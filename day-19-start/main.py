from turtle import Turtle, Screen

mike = Turtle()
screen = Screen()

def move_forward():
    mike.forward(20)
def backward():
    mike.backward(20)
def left():
    mike.left(20)
def right():
    mike.right(20)
def clear_screen():
    mike.reset()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()