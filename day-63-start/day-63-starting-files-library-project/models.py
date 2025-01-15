from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# 1) Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# 2) Main SaveData class
class SaveData:
    def __init__(self, db_path="sqlite:///new-books-collection.db"):
        self.db = SQLAlchemy(model_class=Base)
        self.app = Flask(__name__)
        # Configure the SQLite database
        self.app.config["SQLALCHEMY_DATABASE_URI"] = db_path
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.db.init_app(self.app)

        # Define the Book model inside the class
        class Book(self.db.Model):
            tablename = "books"
            id: Mapped[int] = mapped_column(Integer, primary_key=True)
            title: Mapped[str] = mapped_column(String, nullable=False)
            author: Mapped[str] = mapped_column(String, nullable=False)
            rating: Mapped[float] = mapped_column(Float, nullable=True)

        self.Book = Book  # Expose the Book model for external use

        # Create the table if it doesn't exist
        with self.app.app_context():
            self.db.create_all()

    def add_data(self, title, author, rating):
        """
        Adds a new book entry to the database.
        """
        with self.app.app_context():
            book = self.Book(
                title=title,
                author=author,
                rating=float(rating)  # ensure rating is float
            )
            self.db.session.add(book)
            self.db.session.commit()

    def get_all_books(self):
        """
        Returns all books in the database as a list of dictionaries.
        """
        with self.app.app_context():
            books = self.Book.query.all()
            return [
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "rating": book.rating,
                }
                for book in books
            ]

    def get_single_book(self, book_id):
        """
        Returns a single book object by its ID or None if not found.
        """
        with self.app.app_context():
            return self.db.get_or_404(self.Book, book_id)

    def edit_book_rating(self, book_id, new_rating):
        """
        Updates the rating of the specified book.
        """
        with self.app.app_context():
            book_to_edit = self.db.get_or_404(self.Book, book_id)
            book_to_edit.rating = float(new_rating)  # convert to float
            self.db.session.commit()

    def delete_book(self, book_id):
        """
        Deletes the book with the given ID from the database.
        """
        with self.app.app_context():
            book_to_delete = self.db.get_or_404(self.Book, book_id)
            self.db.session.delete(book_to_delete)
            self.db.session.commit()
