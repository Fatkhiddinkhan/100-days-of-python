from turtle import Turtle
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snakes = []
        self.new_snake = 0
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self,):
        self.xcor = 0
        for snake in range(3):
            self.add_position(snake)

    def add_position(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(x=self.xcor, y=new_snake.ycor())
        self.xcor -= 20
        self.snakes.append(new_snake)
    def extend(self):
        self.add_position(self.snakes[-1].position())
    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
