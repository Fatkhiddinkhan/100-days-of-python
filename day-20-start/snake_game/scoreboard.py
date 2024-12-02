from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.color("white")
        self.num = 0
        self.write(f"Score: {self.num}", True, align="center", font=('Arial', 20, 'normal'))
        self.update()
    def update(self):
        self.goto(0, 275)
        self.clear()
        self.write(f"Score: {self.num}", True, align="center", font=('Arial', 20, 'normal'))
    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", True, align="center", font=('Arial', 20, 'normal'))

    def increment(self):
        self.num += 1
        self.update()
