from turtle import Turtle, Screen
import random


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return turtle.color(r, g, b)


turtle = Turtle()
turtle.speed("fastest")
angle = 0
while angle < 360:
    change_color()
    turtle.right(3)
    turtle.circle(150)
    angle += 3

screen = Screen()
screen.exitonclick()
