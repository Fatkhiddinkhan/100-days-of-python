# Day 62 - Cafe Note-Taking App

## 🌟 Project Overview

This project is a **Cafe Note-Taking App** built with Flask, designed to store and display information about cafes visited. Users can submit details of cafes, including their name, location, opening and closing times, and ratings for coffee quality, WiFi strength, and power socket availability. The data is saved in a CSV file and dynamically rendered for future reference.

---

## 🛠️ Features

### 1. **Add Cafe Form**
The app includes a user-friendly form built with **Flask-WTF** and styled using **Flask-Bootstrap**. Key form features include:
- **Cafe Name**: Input for the name of the cafe.
- **Google Maps Location**: A field for entering the cafe's Google Maps URL, validated with the `URL` validator.
- **Opening and Closing Times**: Input fields for specifying the cafe's operational hours.
- **Ratings**:
  - Coffee Quality (☕️)
  - WiFi Strength (🛜)
  - Power Socket Availability (🔌)
  
  Users can select ratings from 1 to 5, represented visually by icons.

### 2. **Data Storage and Retrieval**
- The app saves user-submitted data to a **CSV file** (`cafe-data.csv`).
- Each row in the CSV file contains details such as cafe name, location, operational hours, and ratings.

### 3. **Display Cafes**
- A **cafes page** dynamically reads the CSV file and displays a table with all the stored cafe data.
- Iconic representations (e.g., ☕️, 🛜, 🔌) are used to visually showcase ratings for coffee, WiFi, and power.

---

## 🖥️ Project Structure

```
├── app.py               # Main Flask app
├── cafe-data.csv        # CSV file for storing cafe data
├── templates
│   ├── base.html        # Base template for layout
│   ├── index.html       # Homepage
│   ├── add.html         # Add Cafe form page
│   ├── cafes.html       # Display cafes page
└── static
    └── styles.css       # Additional CSS (if any)
```

---

## 🚀 How It Works

### Add Cafe
1. Users navigate to the **Add Cafe** page (`/add`).
2. Fill out the form fields, including cafe details and ratings.
3. On submission, the form data is:
   - Validated using **Flask-WTF validators**.
   - Processed and written to `cafe-data.csv` in a structured format.
   - Redirected to the **Cafes Page** to view the updated list.

### Display Cafes
1. Navigate to the **Cafes Page** (`/cafes`).
2. The app reads the CSV file and dynamically renders a table displaying all stored cafes and their respective details.

---

## 🔗 Key Code Highlights

### Form Class with Flask-WTF
```python
class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe location on Google map', validators=[DataRequired(), URL()])
    open_time = TimeField(label='Open', validators=[DataRequired()])
    close_time = TimeField(label='Close', validators=[DataRequired()])
    coffee = SelectField(label="Coffee",
                         choices=[('1', '☕️'),
                                  ('2', '☕️☕️'),
                                  ('3', '☕️☕️☕️'),
                                  ('4', '☕️☕️☕️☕️️'),
                                  ('5', '☕️☕️☕️☕️☕️')],
                         validators=[DataRequired()])
    wifi = SelectField(label="Wifi",
                       choices=[('1', '🛜'),
                                ('2', '🛜🛜'),
                                ('3', '🛜🛜🛜'),
                                ('4', '🛜🛜🛜🛜️'),
                                ('5', '🛜🛜🛜🛜🛜')],
                       validators=[DataRequired()])
    power = SelectField(label="Power",
                        choices=[('1', '🔌'),
                                 ('2', '🔌🔌'),
                                 ('3', '🔌🔌🔌'),
                                 ('4', '🔌🔌🔌🔌️'),
                                 ('5', '🔌🔌🔌🔌🔌')],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')
```

### Writing Data to CSV
```python
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{convert_to_icons(form.coffee.data, '☕️')},"
                           f"{convert_to_icons(form.wifi.data, '🛜')},"
                           f"{convert_to_icons(form.power.data, '🔌️')}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)
```

### Reading and Displaying CSV Data
```python
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)
```

---

## 🎉 Key Learning Points

- **Flask-WTF**: Simplified form creation and validation.
- **CSV Manipulation**: Reading from and writing to CSV files using Python.
- **Dynamic Rendering**: Displaying data dynamically in HTML templates.
- **Icon Mapping**: Converting numeric ratings into icons for better visualization.
- **Bootstrap Integration**: Leveraged Bootstrap for responsive and aesthetic design.

---

## 📂 Future Improvements

- Add a feature to edit or delete existing cafe data.
- Integrate a database (e.g., SQLite) for better scalability and flexibility.
- Enhance form validations to handle edge cases more robustly.

---

This project was a significant step toward building a full-stack web application. It combined backend data processing with a dynamic and visually appealing frontend, showcasing the potential of Flask and Python for rapid web development. 🚀
