import random
import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)
GET_GENDER_URL = "https://api.genderize.io"
GET_AGE_URL = "https://api.agify.io"


@app.route("/")
def home():
    year = datetime.datetime.today().year
    random_number = random.randint(1,20)
    return render_template("index.html", num=random_number, current_year=year)

@app.route("/guess/<name>")
def guess(name):
    parameter = {
        "name": name
    }
    gender_response = requests.get(GET_GENDER_URL, params=parameter)
    age_response = requests.get(GET_AGE_URL, params=parameter)
    age = age_response.json()["age"]
    gender = gender_response.json()["gender"]
    name = name.capitalize()
    return render_template("user.html", name=name, gender=gender, age=age)

@app.route("/blog")
def blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)