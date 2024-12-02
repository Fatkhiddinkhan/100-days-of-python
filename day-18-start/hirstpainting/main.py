# import colorgram
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

mike = Turtle()
mike.penup()
mike.speed("fastest")
mike.hideturtle()
new_colors = [(239, 247, 252), (215, 150, 109), (37, 101, 166), (157, 58, 87), (142, 81, 56), (115, 172, 210), (239, 225, 99), (216, 129, 157), (215, 68, 101), (162, 23, 43), (222, 85, 57), (122, 181, 138), (76, 35, 23), (46, 123, 82), (162, 149, 35), (25, 167, 199), (20, 57, 139), (126, 37, 28), (47, 186, 153), (17, 38, 86), (235, 163, 182), (239, 167, 155), (131, 233, 191), (132, 214, 235), (92, 107, 190), (74, 31, 44), (167, 177, 230)]

#
# rgb_colors = []
# colors = colorgram.extract('fixed_image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     formated_color = (r, g, b)
#     rgb_colors.append(formated_color)
# print(rgb_colors)

start_position = mike.teleport(-250, -240)


dot_size = 20
mike_move = 45
raws = 12
cols = 12
for col in range(cols):
    for raw in range(raws):
        mike.dot(dot_size, random.choice(new_colors))
        mike.forward(mike_move)

    mike.setx(-250)
    mike.sety(mike.ycor() + mike_move)



# mike.teleport(60)
# mike.teleport(y=10)
# print(mike.pos())






screen = Screen()
screen.exitonclick()
