import requests
from flask import Flask, render_template

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts=response)

@app.route("/post/<int:num>")
def post(num):
    link_text = None
    for blog_post in posts:
        if int(blog_post["id"]) == num:
            link_text = blog_post
    return render_template("post.html", post=link_text)

if __name__ == "__main__":
    app.run(debug=True)
