import random
from turtle import Turtle, Screen
is_race = False
screen = Screen()
screen.setup(500, 400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
y_cor = -100
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_cor)
    y_cor += 43
    turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="what turtle will win the race. Chose the color:")
print(user_bet)

if user_bet:
    is_race = True

while is_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The {winning_color} turtle is the winner")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()