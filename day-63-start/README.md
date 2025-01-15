# Flask Book Library

This is a simple Flask application that lets you manage a library of books. You can add new books, edit a book’s rating, and delete books from your collection. We use an SQL database (SQLite) to store and retrieve book data.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Database & SQL](#database--sql)
- [Learning Notes](#learning-notes)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project was built as part of my Python learning journey and marks the end of Day 63. It demonstrates how to:

- Create tables for books and handle all CRUD operations (Create, Read, Update, Delete).
- Use Jinja2 templates to render data on the front end.
- Pass query parameters to handle specific database operations (e.g., edit a particular book by ID).

You can upload this project to GitHub every day to track progress and changes over time. Completing this project involved overcoming challenges such as:

- Understanding how to integrate Flask with a SQL database.
- Debugging issues with database migrations.
- Implementing dynamic rendering of templates using Jinja2.

## Features

- **Home Page**: Displays a list of all books with their title, author, and rating.
- **Add Book**: Provides a form to add a new book to the database.
- **Edit Rating**: Allows you to update the rating of a specific book.
- **Delete Book**: Lets you remove a book from the library altogether.

## Technologies Used

- **Python 3**
- **Flask** (with Jinja2 templates)
- **SQLAlchemy** (ORM)
- **SQLite** (as the SQL database)

## Project Structure

```plaintext
your_project/
├── app.py               # Flask routes (home, add, edit, delete)
├── models.py            # Contains the SaveData class for DB handling
├── requirements.txt     # Python dependencies (optional)
└── templates/
    ├── index.html       # Displays all books
    ├── add.html         # Form to add a new book
    └── edit.html        # Form to edit a book's rating
```

## Getting Started

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run `app.py` to start the Flask server.
4. Open `http://127.0.0.1:5000/` in your web browser to access the application.

## Database & SQL

The application uses SQLite as the database to store book information. SQLAlchemy is used as the ORM to interact with the database, providing an abstraction layer over SQL queries.

## Learning Notes

This project emphasizes the following concepts:

- Integrating Flask with a SQL database.
- Creating and rendering templates using Jinja2.
- Handling GET and POST requests for CRUD operations.
- Managing database schema and query execution with SQLAlchemy.

## Contributing

Contributions are welcome! If you’d like to improve this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
