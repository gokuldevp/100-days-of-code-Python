from turtle import Turtle, Screen
import random

turtle = Turtle()

for side in range(3, 11):
    R = random.random()
    B = random.random()
    G = random.random()
    angle = 360/side
    turtle.color(R, G, B)
    for move in range(side):
        turtle.forward(100)
        turtle.right(angle)
screen = Screen()
screen.exitonclick()
