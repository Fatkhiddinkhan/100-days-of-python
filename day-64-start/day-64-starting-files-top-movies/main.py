"""
This module sets up the Flask application, routes, and initializes the database and manager classes.
"""

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


from modul import MovieManager, FormManager, AddMovie, MovieData

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    pass

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///favourite-movies.db"
db = SQLAlchemy(model_class=Base)
Bootstrap5(app)

# Initialize the managers
movie_mg = MovieManager(db, app)
search_movie = MovieData()


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home route:
      - If GET without an "id" param, displays all movies.
      - If "id" is present, fetches that movie from TMDB, adds it, and redirects to edit.
    """
    # Display all movies if there's no "id" param
    if request.method == "GET" and not request.args.get("id"):
        all_movies = movie_mg.get_all_movies()
        return render_template("index.html", movies=all_movies)

    # If there's a movie ID, fetch details, add it, then redirect to edit
    movie_id = request.args.get("id")
    if movie_id:
        movie_details = search_movie.get_movie_detail(movie_id)
        new_id = movie_mg.add_new_movie(
            title=movie_details[0],
            year=movie_details[1],
            description=movie_details[2],
            img_url=movie_details[3]
        )
        return redirect(url_for("edit", id=new_id))

    # Fallback
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    """
    Route to add a new movie:
      - Shows a form where the user can enter a movie title.
      - On form submission, fetches matching results from TMDB and displays them.
    """
    form = AddMovie()
    if form.validate_on_submit():
        movie_query = form.new_movie.data
        movies = search_movie.get_movies(movie_query)
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)


@app.route("/select")
def select():
    """
    Route for displaying movie search results.
    Typically loaded after the user submits a search in /add.
    """
    return render_template("select.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    """
    Route to edit a movie's rating and review.
    The movie ID is passed as a query parameter ("id").
    """
    form = FormManager()
    movie_id = request.args.get("id")

    if form.validate_on_submit():
        new_review = form.new_review.data
        new_rating = form.new_rating.data
        movie_mg.edit_movie_rating(title=movie_id, new_rating=new_rating, new_review=new_review)
        return redirect(url_for("home"))

    return render_template("edit.html", form=form)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    """
    Route to delete a movie from the database.
    The movie ID is passed as a query parameter ("id").
    """
    movie_id = request.args.get("id")
    movie_mg.delete_movie(movie_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
