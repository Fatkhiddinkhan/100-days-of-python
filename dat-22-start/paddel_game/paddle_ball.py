from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.go_x = 10
        self.go_y = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.go_x
        new_y = self.ycor() + self.go_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.go_y *= -1

    def bounce_x(self):
        self.go_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1

        self.bounce_x()