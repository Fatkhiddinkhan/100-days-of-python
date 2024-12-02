import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
mike = Turtle()
mike.color("burlywood4")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_tuple = (r, g, b)
    return new_tuple
mike.speed(0)

def draw (size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        mike.color(random_color())
        mike.circle(100)
        current_position = mike.heading()
        mike.setheading(current_position + size_of_gap)

draw(5)

screen = Screen()
screen.exitonclick()

