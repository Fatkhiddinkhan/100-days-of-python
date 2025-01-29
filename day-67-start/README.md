# 📅 Day 67: Advanced Flask Blog with CRUD Functionality

Today, I took my **personal blog project** to the next level by integrating **full CRUD (Create, Read, Update, Delete) functionality** with an SQL database. This means I can now **add, edit, and delete blog posts**, and all changes are stored persistently in an SQLite database.

---

## 🚀 Features Implemented

### ✅ **Reading Blog Posts**
- **`/` (Home Page)** - Fetches and displays all blog posts from the database.
- **`/show_post/<post_id>`** - Displays an individual blog post based on its ID.

### ✅ **Creating New Blog Posts**
- **`/new-post`** - A form-powered page where users can create and submit new blog posts.
- Posts include:
  - **Title**
  - **Subtitle**
  - **Author Name**
  - **Image URL**
  - **Body Content (Using CKEditor for rich-text editing)**
  - **Auto-generated Date**

### ✅ **Updating Blog Posts**
- **`/edit-post/<post_id>`** - Allows users to edit existing blog posts.
- The form pre-fills with existing post data, making editing seamless.
- After submission, the updated content is saved in the database.

### ✅ **Deleting Blog Posts**
- **`/delete/<post_id>`** - Deletes a blog post from the database.
- Redirects back to the home page after successful deletion.

---

## 🛠️ **Technologies & Tools Used**
- **Flask** - Backend framework for handling routes and database interactions.
- **Flask-WTF & WTForms** - Used for form validation and handling user input.
- **Flask-CKEditor** - Implemented a rich-text editor for writing blog posts.
- **Flask-SQLAlchemy** - Used to manage the SQLite database for storing blog posts.
- **Bootstrap 5** - Enhanced the frontend with responsive design elements.

---

## 🔥 Challenges & Lessons Learned
📌 **Database Structuring** - Learned how to properly define and manage SQLAlchemy models.  
📌 **Handling Forms** - Integrated Flask-WTF forms with pre-populated data for easy editing.  
📌 **Dynamic URL Routing** - Used dynamic routes to handle editing and deleting specific blog posts.  
📌 **Frontend Enhancement** - Improved user experience with Bootstrap and CKEditor for better content formatting.  

---

This project has given me a strong foundation in **Flask-based web development**. I’m excited to keep refining it and eventually deploy the blog as a fully functional web app! 🚀🔥
