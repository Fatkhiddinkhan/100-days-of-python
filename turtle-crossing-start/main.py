import time
from random import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.create_car()
    for car in cars.cars:
        if car.distance(player) < 30:
            print("collided")
            score.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.refresh()
        cars.increment()
        score.update()


screen.exitonclick()
