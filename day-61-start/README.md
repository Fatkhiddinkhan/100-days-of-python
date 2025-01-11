# Flask Login App

## 🌟 Project Overview

This project is a **Flask Login App** built to demonstrate the integration of **Flask-WTF** forms and **Flask-Bootstrap** to create a user authentication system. It includes features such as form validation, secure handling of user inputs, and dynamic content rendering with Flask templates.

---

## 🛠️ Features

1. **Login Form**
   - Built using **Flask-WTF** for simplicity and security.
   - Validates user input fields such as email and password.
   - Uses **Bootstrap** for a responsive and modern design.

2. **Form Validation**
   - Ensures that the email field is correctly formatted.
   - Password field requires input with a validation check.

3. **Dynamic Routing**
   - Users are redirected to a **success page** if the login credentials are correct.
   - Incorrect credentials redirect users to an **access denied page** with a playful GIF.

4. **Reusable Templates**
   - Utilizes Flask's template inheritance and `{% extends %}` to build modular and reusable components for pages.

5. **Responsive Design**
   - The app leverages **Flask-Bootstrap** for a fully responsive design that works seamlessly on any device.

---

## 🔗 Technologies Used

- **Flask**: Python microframework for web development.
- **Flask-WTF**: Simplified form handling with built-in CSRF protection and validation.
- **Flask-Bootstrap**: Integration of Bootstrap CSS for styling and layout.
- **HTML/Jinja**: Template rendering for dynamic content.
- **Python**: Core backend logic and form validation.

---

## 🚀 How It Works

1. **Homepage**:
   - The main entry point (`/`) directs users to a simple landing page.

2. **Login Page**:
   - Accessed via `/login` route.
   - Displays a login form created using Flask-WTF.
   - Validates user input and authenticates based on predefined credentials:
     - **Email**: `admin@email.com`
     - **Password**: `12345678`

3. **Success Page**:
   - If login credentials are correct, users are directed to a success page.

4. **Access Denied Page**:
   - Incorrect credentials lead to an access denied page with a humorous GIF.

---

## 🖥️ Project Structure

```
├── app.py               # Main Flask app
├── templates
│   ├── base.html        # Base template for layout
│   ├── index.html       # Homepage
│   ├── login.html       # Login page
│   ├── success.html     # Success page
│   ├── denied.html      # Access denied page
└── static
    └── styles.css       # Additional CSS (if any)
```

---

## 🛠️ Code Highlights

### Flask-WTF Form Example
```python
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")
```

### Login Route with Form Validation
```python
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)
```

---

## 🎉 Key Learning Points

- **Flask-WTF**: Simplified form creation and validation.
- **Bootstrap Integration**: Improved UI/UX with responsive and reusable components.
- **Template Inheritance**: Leveraged `{% extends %}` to maintain clean and DRY code.
- **Routing and Validation**: Implemented dynamic routing and secure input handling.

---

## 📂 Future Improvements

- Add user registration functionality.
- Integrate a database for storing user credentials.
- Implement hashed password storage for enhanced security.
- Expand access levels for different user roles.

---

This project showcases how Flask and its extensions can be used to build robust, secure, and responsive web applications. 🚀
