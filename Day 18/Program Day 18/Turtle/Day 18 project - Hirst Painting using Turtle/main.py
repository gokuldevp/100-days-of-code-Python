from turtle import Turtle, Screen
import random


def color_change():
    r = random.random()
    g = random.random()
    b = random.random()
    return turtle.color(r, g, b)


turtle = Turtle()
turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.setheading(0)
turtle.width(20)
turtle.color("white")


def line():
    for move in range(10):
        turtle.forward(1)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        color_change()


def direction():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)


for back in range(9):
    line()
    turtle.penup()
    turtle.back(51*10)
    direction()







screen = Screen()
screen.exitonclick()
