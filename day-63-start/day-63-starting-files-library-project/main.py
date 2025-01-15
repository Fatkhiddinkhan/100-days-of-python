from flask import Flask, render_template, request, redirect, url_for
from models import SaveData

# 1) Create the database manager
db_manager = SaveData()
# 2) The main Flask app is available as db_manager.app
app = db_manager.app
print(app.template_folder)

@app.route('/')
def home():
    """
    Displays all books on the home (index) page.
    """
    all_books = db_manager.get_all_books()
    return render_template("index.html", all_books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Displays a form to add a new book (GET)
    and handles the book creation (POST).
    """
    if request.method == "POST":
        book_name = request.form.get("book_name")
        book_author = request.form.get("book_author")
        rating = request.form.get("rating")
        db_manager.add_data(title=book_name, author=book_author, rating=rating)
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    """
    GET: Show the 'edit.html' with the requested book data.
    POST: Take the new rating, update the database, then redirect to home.
    """
    if request.method == "GET":
        # 1. Get the book ID from the query parameters e.g. /edit?book_id=5
        book_id = request.args.get("book_id", None)
        # 2. If there's no book_id, redirect home
        if not book_id:
            return redirect(url_for("home"))
        # 3. Convert to int (assuming your 'id' is integer)
        try:
            book_id = int(book_id)
        except ValueError:
            return redirect(url_for("home"))

        # 4. Get the actual book from DB
        book = db_manager.get_single_book(book_id)
        # 5. Render 'edit.html' passing the book data
        return render_template("edit.html", book=book)

    # If request.method == "POST":
    # => This is when user has submitted a new rating
    book_id = request.form.get("id")
    new_rating = request.form.get("rating")
    if not book_id or not new_rating:
        return redirect(url_for("home"))

    try:
        book_id = int(book_id)
        new_rating = float(new_rating)
    except ValueError:
        # If conversion fails, go home or handle error
        return redirect(url_for("home"))

    db_manager.edit_book_rating(book_id, new_rating)
    return redirect(url_for("home"))

@app.route("/delete", methods=["GET"])
def delete_book():
    """
    Reads "book_id" from query params and deletes that book,
    then redirects back to the homepage.
    """
    book_id = request.args.get("book_id")
    try:
        book_id = int(book_id)
    except ValueError:
        return redirect(url_for("home"))

    db_manager.delete_book(book_id)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
