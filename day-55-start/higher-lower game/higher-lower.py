import random

from flask import Flask
GIF = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmVva2w2Y255ZGhwNmw5MTJ6NXk5NnpyejdmeDRqNW16NGhnZWU5bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif"

app = Flask(__name__)
def get_random_number():
    random_number = random.randint(0, 9)
    return random_number
ran_num = get_random_number()
print(ran_num)

def higher_lower(func):
    def wrapper(*args,  **kwargs):
        result = func(*args,  **kwargs)
        if result > ran_num:
            return (f"<h1>Too high. Try again.</h1>"
                    f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>")
        elif result < ran_num:
            return (f"<h1>Too low. Try again.</h1>"
                    f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>")
        elif result == ran_num:
            return (f"<h1>You found me</h1>"
                    f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>")
        else:
            return f"Invalid input. Try again"
    return wrapper

@app.route("/")
def home():
    return (f"<h1> Guess a random number between 0 and 9:</h1>"
            f"<img src={GIF}>")

@app.route("/<int:number>")
@higher_lower
def user_guess(number):
    return number

@app.route("/new_game")
def new_game():
    global ran_num  # Access the global variable
    ran_num = random.randint(0, 9)  # Generate a new random number
    print(f"New random number: {ran_num}")
    return (f"<h1>New Game Started! Guess a number between 0 and 9:</h1>"
            f"<img src={GIF}>")

if __name__ == "__main__":
    app.run(debug=True)