from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def home():
    return "this is a home"

if __name__ == "__main__":
    app.run()

import time

def speed_calc_decorator(function):
    def wrapper():
        print("Wrapper starts")
        start_time = time.time()  # Start timing
        function()  # Call the original function
        end_time = time.time()  # End timing
        print(f"{function.__name__} run speed: {end_time - start_time}s")
        print("Wrapper ends")
    return wrapper

@speed_calc_decorator
def fast_function():
    print("Inside fast_function")
    for i in range(1000000):
        i * i

fast_function()