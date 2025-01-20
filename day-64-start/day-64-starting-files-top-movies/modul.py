"""
Module containing classes and forms for movie management and external movie data retrieval.

Classes:
- MovieManager: Handles Movie database operations (CRUD).
- FormManager: A FlaskForm for editing a movie's rating and review.
- AddMovie: A FlaskForm for adding a movie by title.
- MovieData: Handles interaction with TheMovieDB (TMDB) API.
"""
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

API_KEY = os.environ.get("API_KEY")
URL = "https://api.themoviedb.org/3/search/movie"


class MovieManager:
    """
    Manages Movie records in the database, including creation, querying, updating, and deletion.
    """

    def __init__(self, db, app):
        self.db = db
        self.app = app
        self.db.init_app(self.app)
        self.Movies = None

        # Define the Movie model within this class
        class Movie(self.db.Model):
            """
            Represents a Movie record with fields for
            title, year, description, rating, ranking, review, and img_url.
            """
            id: Mapped[int] = mapped_column(Integer, primary_key=True)
            title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
            year: Mapped[int] = mapped_column(Integer, nullable=True)
            description: Mapped[str] = mapped_column(String, nullable=False)
            rating: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
            ranking: Mapped[int] = mapped_column(Integer, nullable=True)
            review: Mapped[str] = mapped_column(String, nullable=False, default="No review yet")
            img_url: Mapped[str] = mapped_column(String, nullable=False)

        self.Movies = Movie

        # Create table if not already present
        with self.app.app_context():
            self.db.create_all()

    def add_new_movie(self, title, year, description, img_url, rating=None, ranking=None, review=None):
        """
        Adds a new movie to the database and returns its auto-generated ID.
        """
        with self.app.app_context():
            new_movie = self.Movies(
                title=title,
                year=year,
                description=description,
                rating=rating,
                # ranking=ranking,
                review=review,
                img_url=img_url
            )
            self.db.session.add(new_movie)
            self.db.session.commit()

        # Retrieve the newly added movie to get its ID
        result = self.db.session.execute(
            self.db.select(self.Movies).filter_by(title=title)
        ).scalar()
        return result.id

    def get_movie(self, title):
        """
        Retrieves a Movie by its unique title.
        """
        with self.app.app_context():
            result = self.db.session.execute(
                self.db.select(self.Movies).filter_by(title=title)
            ).scalar()
            return result

    def get_all_movies(self):
        """
        Retrieves all movies from the database ordered by rating (ascending).
        Then updates each movie's ranking (descending) and returns the list of movies.
        """
        with self.app.app_context():
            # Query all movies ordered by rating
            movies = self.db.session.execute(
                self.db.select(self.Movies).order_by(self.Movies.rating)
            ).scalars().all()

        # Update ranking in descending order
        for n in range(len(movies)):
            movies[n].ranking = len(movies) - n

        # Commit changes to persist updated ranking
        self.db.session.commit()
        return movies

    def edit_movie_rating(self, title, new_rating, new_review):
        """
        Updates a specific movie's rating and review, looked up by title.
        """
        with self.app.app_context():
            movie = self.db.get_or_404(self.Movies, title)
            movie.rating = new_rating
            movie.review = new_review
            self.db.session.commit()

    def delete_movie(self, movie_id):
        """
        Deletes a movie from the database by its ID.
        """
        with self.app.app_context():
            movie = self.db.get_or_404(self.Movies, movie_id)
            self.db.session.delete(movie)
            self.db.session.commit()

class FormManager(FlaskForm):
    """
    Form used to update an existing movie's rating and review.
    """
    new_rating = FloatField(label="Your new rating from 1 to 10", validators=[DataRequired()])
    new_review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

class AddMovie(FlaskForm):
    """
    Form used to add a new movie to the database by searching its title.
    """
    new_movie = StringField(label="Movie title", validators=[DataRequired()])
    submit = SubmitField(label="Add movie")

class MovieData:
    """
    Handles interactions with TheMovieDB (TMDB) API for searching and fetching movie details.
    """

    def __init__(self):
        self.api_key = API_KEY
        self.url = URL
        # Print the API key for debugging purposes (optional)
        print(repr(API_KEY))

    def get_movies(self, title):
        """
        Searches TMDB for movies matching the given title.
        Returns a list of results (dict objects).
        """
        params = {
            "api_key": self.api_key,
            "query": title,
            "language": "en-US",
            "include_adult": "true",
            "region": "US",
        }
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            print(f"Error: {response.status_code} - {response.reason}")

    def get_movie_detail(self, movie_id):
        """
        Retrieves detailed information for a single movie by its ID from TMDB.
        Returns a list [title, year, description, img_url] if successful, or None if there's an error.
        """
        detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        params = {
            "api_key": self.api_key,
            "language": "en-US"
        }
        response = requests.get(detail_url, params=params)
        if response.status_code == 200:
            movie = response.json()
            title = movie["original_title"]
            year = movie["release_date"].split("-")[0]
            description = movie["overview"]
            img = f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}"
            return [title, year, description, img]
        else:
            print(f"Error: {response.status_code} - {response.reason}")
            return None
