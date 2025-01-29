# 📅 Day 66: Learning API Development with Flask & Using Postman

Today, I worked on building a **Flask-based REST API** for managing a **Cafe database**. This was a hands-on project that involved setting up an SQLite database using **SQLAlchemy**, defining a **Cafe model**, and implementing various API endpoints to interact with the database.

## 🚀 Key Features Implemented

### ✅ GET Requests
- **`/random`** - Fetches a random cafe from the database.  
- **`/get_all`** - Retrieves all cafes in JSON format.  
- **`/search?loc=<location>`** - Searches for cafes in a specific location.

### ✅ POST Request
- **`/add`** - Allows users to add a new cafe by submitting form data.

### ✅ PATCH Request
- **`/update-price/<cafe_id>?new_price=<price>`** - Updates the coffee price of a specific cafe.

### ✅ DELETE Request
- **`/report-closed/<cafe_id>?api_key=<key>`** - Deletes a cafe from the database (requires an API key for authorization).

---

## 🛠️ Postman & API Documentation

Today, I also learned how to use **Postman** to test and document API requests. I practiced:

✔ Sending **GET, POST, PATCH, and DELETE** requests.  
✔ Using **query parameters** for filtering data.  
✔ Handling **API authentication** with an API key.  
✔ Documenting API responses to create **structured API documentation**.

---

## 🔥 Challenges & Lessons Learned

📌 **Handling Boolean Data**: Converting form input into `True`/`False` values required explicit casting.  
📌 **Debugging API Responses**: Using Postman helped visualize the JSON responses and debug errors efficiently.  
📌 **Error Handling**: Implemented custom error messages for missing data and unauthorized actions.  

---

This marks another step towards mastering backend development and API integration! Looking forward to building more complex APIs and integrating them with frontends in the upcoming days. 🚀
