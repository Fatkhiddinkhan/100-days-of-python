# Day 57 - Jinja Framework and Flask Blog Website

## 🌟 What I Learned Today

Today, I dived deeper into **Flask** and explored the **Jinja Framework**, a powerful templating engine for Python web development. Jinja allows us to dynamically insert Python code directly into HTML files, enabling the creation of dynamic and interactive web pages. Some key concepts I learned include:

- How to use Jinja's templating syntax (``{{ ... }}`` and ``{% ... %}``) to dynamically render content in HTML.
- Utilizing Python data directly in HTML templates for better functionality and flexibility.

## 🖥️ What I Built Today

### 1. Dynamic Number and Year Display
Using Jinja and Python, I created a homepage that dynamically displays:
- A random number between 1 and 20.
- The current year fetched using Python's `datetime` module.

This demonstrates how Python code can seamlessly interact with HTML using Jinja.

---

### 2. Guess the User's Age and Gender
I built a fun feature using two public APIs:
- **Agify API** for guessing a person's age based on their name.
- **Genderize API** for guessing a person's gender based on their name.

The user can input their name, and the app dynamically fetches their estimated age and gender, rendering the results using Jinja in a user-friendly format.

---

### 3. A Fully Functional Blog Website
The highlight of today was creating a **blog website** using Flask and Jinja! 

- **Blog Data**: The blog content is dynamically fetched from an API endpoint: `https://api.npoint.io/c790b4d5cab58020d391`.
- **Home Page**: Displays a list of blog posts with a title, description, and a "Read" button.
- **Post Page**: Clicking "Read" takes the user to a detailed page about that specific blog post, dynamically rendered based on its ID.

