import colorgram                                                          # used to import color from image
from turtle import Turtle, Screen, colormode
import random

# colors = colorgram.extract('hiest.jpg', 31)
#
# available_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     available_colors.append(rgb)
# print(available_colors)

color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82), (115, 134, 139)]


colormode(255)
turtle = Turtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)


def line():
    for num in range(10):
        turtle.dot(20, random.choice(color_list))
        turtle.forward(50)


def direction():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)


for back in range(10):
    line()
    turtle.penup()
    turtle.back(50*10)
    direction()


screen = Screen()
screen.exitonclick()
