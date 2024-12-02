from fcntl import FASYNC
from turtle import Screen
import time
import functionality
from food import Food
from scoreboard import Score

screen = Screen()
food = Food()
score = Score()


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = functionality.Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_snake()
        score.increment()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()
    snake.move()
















screen.exitonclick()