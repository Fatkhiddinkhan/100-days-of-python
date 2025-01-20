# Day 64: Creating Favorite Movies Web App

Welcome to the **Favorite Movies Web App**! This project is part of my 100 Days of Python challenge and showcases a Flask application I built to practice full-stack development with Python, Flask, and SQLAlchemy.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Key](#api-key)
- [Credits](#credits)
- [License](#license)

## Overview

This web app allows you to:

- Search for movies using The Movie Database (TMDB) API.
- Add movies to your personal favorites list.
- Rate and review movies.
- Delete unwanted entries from the list.

All interactions are managed by a Flask back-end using SQLAlchemy with SQLite for data storage.

## Features

### Home Page
- Displays a list of your favorite movies, sorted by rating (ascending).
- Each movie's ranking is updated automatically based on its position in the sorted list (descending order).

### Add a Movie
- Search for a movie by title using a simple form.
- View matching search results and select a movie to add to your favorites.

### Edit a Movie
- Rate the movie on a scale of 1 to 10.
- Provide a personalized review.

### Delete a Movie
- Removes the movie from the database entirely.

## Technologies Used

- **Python 3**
- **Flask**: For creating the web application.
- **Flask-Bootstrap**: For styling the front-end easily.
- **Flask-WTF**: For managing web forms.
- **SQLAlchemy**: For object-relational mapping (ORM) with a SQLite database.
- **TMDB API**: For fetching movie data (search, details, etc.).

## Project Structure

```
.
├── app.py          # Main Flask application setup & routes
├── modul.py        # Contains classes and forms for movie management 
│                   # and TMDB data retrieval
├── templates/
│   ├── base.html   # 
│   ├── index.html  # Displays the list of movies
│   ├── add.html    # Form for adding a movie (search by title)
│   ├── select.html # Displays search results from TMDB
│   └── edit.html   # Form for editing a movie's rating and review
├── static/
│   └── ...         # Static files (CSS, images, if any)
└── README.md       # Project documentation (you are here)
```

## Usage

1. Clone or download the repository to your local machine.
2. Make sure you have Python installed and set up a virtual environment.
3. Install the required dependencies using `pip install - requirements.txt`
4. Run the application:

   ```bash
   python app.py
   ```

5. Open your browser to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and enjoy:
   - View your favorite movies.
   - Add new movies using the search functionality.
   - Edit ratings and reviews or delete movies as needed.

## API Key

The application uses TMDB (The Movie Database) for movie data. To run the app:

1. Create a TMDB account and obtain an API key.
2. Add your TMDB API key to your environment variables:

   ```bash
   # On Mac/Linux
   export API_KEY="YOUR_TMDB_API_KEY"

   # On Windows
   set API_KEY="YOUR_TMDB_API_KEY"
   ```

3. Alternatively, you can hardcode your key in `modul.py` by replacing:

   ```python
   API_KEY = os.environ.get("API_KEY")
   ```

   with:

   ```python
   API_KEY = "YOUR_TMDB_API_KEY"
   ```

   *(Note: Hardcoding API keys is not recommended for production or public repositories.)*

## Credits

- **Flask** – [Documentation](https://flask.palletsprojects.com/)
- **SQLAlchemy** – [Documentation](https://docs.sqlalchemy.org/)
- **TMDB API** – [The Movie Database](https://www.themoviedb.org/documentation/api)
- Special thanks to the 100 Days of Code community for ongoing support and learning resources!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy coding! I hope you find this mini-project useful and continue enjoying the journey through 100 Days of Python.
