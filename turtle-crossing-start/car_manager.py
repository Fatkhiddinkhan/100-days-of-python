import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.increase_speed = MOVE_INCREMENT
        self.starting_speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 5:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(x=270, y=random.randint(-255, 280))
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.starting_speed )


    def increment(self):
        self.starting_speed += self.increase_speed
