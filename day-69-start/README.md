# Personal Blog Web App – Day 69

I’ve just wrapped up **Day 69** of my 100 Days of Code, and the focus was on enhancing my personal blog web app built with Flask. This project incorporates:

- **Flask** for handling routes and rendering templates.
- **SQLAlchemy** for database operations.
- **Flask-Login** for user authentication and access control.
- **Email verification** to ensure only real users can register (an email with a unique code is sent to confirm identity).
- **Bootstrap** for quick styling and responsive layouts.
- **CKEditor** for rich-text editing in blog posts.

## Key Accomplishments
1. **Finished a Personal Blog**: Set up a fully functional blog with the ability to create, read, update, and delete posts (CRUD).
2. **User Authentication**:
   - **Registration**: Users can sign up with an email and password, which is securely hashed and stored.
   - **Email Verification**: A unique code is sent to the user’s email. They must enter the code to complete registration.
   - **Login/Logout**: Managed by Flask-Login, ensuring a seamless user experience.
3. **Challenges**:
   - **Database Table Connections**: Faced some hurdles linking the user, blog post, and comment models, but resolved them with SQLAlchemy relationships.
   - **Flask-Login Integration**: Ensured unauthorized users cannot perform admin-level tasks like creating, editing, or deleting posts.

Through these challenges, I’ve deepened my knowledge of how Flask works with databases, user sessions, and email handling. 

## Project Structure
Here’s a quick overview of how the project is organized:

- **`main.py`**: Main application file containing routes, database models, and initialization code.
- **`forms.py`**: Contains WTForms classes for registration, login, blog post creation, etc.
- **Templates** (HTML files): For pages like home (`index.html`), login, register, email verification, and blog post details.
- **Static** (CSS/JS/img files): For pages like home (`index.html`), login, register, email verification, and blog post details.
- **Instance** (DataBase files): To save user data, like: user registration info, user posts, comments
