from flask import Flask, render_template
import requests
app = Flask(__name__)

#-------API request------#
articles = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
@app.route("/")
def home():
    return render_template("index.html", articles=articles)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def post(num):
    requested_post = None
    for article in articles:
        if article["id"] == num:
            requested_post = article

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)

