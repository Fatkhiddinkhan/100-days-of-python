import time
from turtle import Screen, Turtle
from paddles import Paddle
from paddle_ball import Ball
from score_board import Score
screen = Screen()
screen.tracer(0)
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
r_paddle = Paddle(position=350)
l_paddle = Paddle(position=-350)
score = Score()

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < - 320:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        score.r_point()



















screen.exitonclick()