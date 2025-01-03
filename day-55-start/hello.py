from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def mane_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper

def make_underline(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1>Hello World<h1>"

@app.route("/bey")
@make_bold
@mane_emphasis
@make_underline
def bey():
    return "<p>Good Bey<p>"

@app.route("/username/<name>/<int:random_number>")
def user(name, number):
    return (f"<h1 style='text-align: center'> Hello {name}</h1>"
            f"<p style='text-align: center'>You are {number} years old</p>"
            f"<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXF4ZnZ1ZXV2azc2NGJ3dnB6Mnhtbng3azdyZWdqdzNoeWVuZXpwaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tHIRLHtNwxpjIFqPdV/giphy.gif' width=400>")

if __name__ == "__main__":
    app.run(debug=True)