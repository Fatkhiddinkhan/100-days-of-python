# Day 60 - Enhancing the Flask Blog Project

## 🌟 What I Learned Today

Today, we worked on improving our **Day 59 Flask blog project** by implementing a **Contact Form** and enabling it to send emails using the **SMTP library**. This added a fully functional user interaction feature, where visitors can submit their details and a message, which is then sent directly to the website owner's email.

---

## 🖥️ Features Added

### 1. **Contact Form**
We created a contact form on the `contact.html` page where users can input:
- **Name**
- **Email**
- **Phone**
- **Message**

The form is structured to collect user input, which is sent to the server when submitted.

---

### 2. **SMTP Email Integration**
The collected data from the contact form is processed on the server using Flask's `request` module. Here’s how it works:
1. **Fetching Form Data**:
   - User input is captured using `POST` method and Flask's `request.form` functionality.
2. **Email Sending**:
   - Used Python's **SMTP library** to send the form data as an email.
   - Configured the email client to use Gmail’s SMTP server (`smtp.gmail.com`) with secure login via `starttls`.

---

## ✅ Accomplishments

- **Dynamic Contact Form**: Users can now interact with the blog by submitting their details and feedback.
- **Automated Email Notifications**: Form submissions are sent directly to the blog admin's email in a structured format.
- **Improved User Experience**: Added feedback to the user after form submission (`msg_sent` variable), notifying them whether their message was successfully sent.

---

## 🛠️ Code Highlights

### Contact Form Route:
The `/submit` route handles the form submission:
```python
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        form = f"{name}\n{email}\n{phone}\n{message}"
        with smtplib.SMTP("smtp.gmail.com.") as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=MY_TOKEN)
            connection.sendmail(from_addr=MY_GMAIL,
                                to_addrs=MY_GMAIL,
                                msg=f"Subject:From Blog\n\n{form}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
