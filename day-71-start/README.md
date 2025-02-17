# 📝 Day 71 - Personal Blog Project (Real-World Application) 🚀  

### 🌟 Overview  
Today, I **completed and deployed** my biggest real-world project so far: **a personal blog**. This project is now fully functional and ready to use. I learned how to **deploy applications using free hosting services like Heroku** and also implemented an **additional security feature** to prevent bots and fake users by adding **email verification**.

---

## 🔧 Tech Stack & Tools  
- **Python (Flask/Django)** – Backend framework  
- **SQLite/PostgreSQL** – Database management  
- **Jinja2** – Templating engine  
- **HTML, CSS, Bootstrap** – Frontend styling  
- **SMTP (smtplib)** – Email verification system  
- **Heroku** – Deployment platform  

---

## 🚀 Key Features  

### 🏡 **1. Personal Blog Functionalities**  
✔️ Users can create an account and log in.  
✔️ Selected Users can create, edit, and delete blog posts.  
✔️ Blogs are displayed in a user-friendly format.  
✔️ Responsive UI with Bootstrap.  

### 🔒 **2. Email Verification System (Custom Implementation)**  
To **prevent spam/bots** and ensure only real users sign up, I implemented **email verification** using Python’s `smtplib` library:  
✔️ When a user registers, a **6-digit code** is sent to their email.  
✔️ The user **must enter the code** to verify their email before gaining access.  
✔️ This helps **prevent fake accounts** from interacting with my blog.  

**📌 Code Snippet for Email Verification:**  
## 🌍 **Deployment - How I Hosted It on Heroku**  
I deployed my blog using **Heroku**, a free hosting platform for web applications.  

Now, my **personal blog is live** and can be accessed anywhere! 🚀  

---

## 🔥 Lessons Learned & Takeaways  
✔️ **Building a real-world project** helps solidify concepts learned in tutorials.  
✔️ **Deployment** is a crucial step in development. Heroku provides a great free solution.  
✔️ **Security is important** – implementing email verification protects against spam accounts.  
✔️ **SMTP (smtplib) is powerful** for sending automated emails directly from Python.  

---

## 📂 Repository Content  
- Full source code for the **personal blog** project  
- Email verification implementation  
- Deployment documentation  

---

## 🎯 Next Steps  
Now that my **personal blog** is live, I plan to:  
✅ Optimize it with **better UI and UX improvements**.  
✅ Implement **password reset functionality**.  
✅ Explore **more hosting options** (e.g., **Railway, Vercel**).  
✅ Expand my blog by adding **user comments and likes**.  

---

🔗 **Stay tuned for more updates as I continue my 100 Days of Python journey!** 🚀  
