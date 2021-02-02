import random
from turtle import Turtle, Screen


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return turtle.color(r, g, b)


turtle = Turtle()
screen = Screen()
turtle.width(10)
turtle.speed("fastest")
angle_list = [0, 90, 180, 270]
num = random.randrange(10, 50, 10)
for move in range(num):
    change_color()
    distance = random.randrange(10, 50, 10)
    angle = random.choice(angle_list)
    turtle.forward(distance)
    turtle.setheading(angle)

screen.exitonclick()
