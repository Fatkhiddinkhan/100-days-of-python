from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.num = 0
        self.goto(x=-230, y=270)
        self.write(f"Level: {self.num}", True, align="center", font=(FONT))
    def update(self):
        self.goto(x=-230, y=270)
        self.clear()
        self.num += 1
        self.write(f"Level: {self.num}", True, align="center", font=(FONT))
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER: {self.num}", True, align="center", font=(FONT))

