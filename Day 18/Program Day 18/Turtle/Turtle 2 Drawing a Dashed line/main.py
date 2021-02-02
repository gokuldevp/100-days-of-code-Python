from turtle import Turtle, Screen

gokul = Turtle()
nanu = Turtle()
nanu.right(90)
for move in range(15):
    gokul.forward(10)
    gokul.color("white")
    gokul.forward(10)
    gokul.color("black")
    nanu.forward(10)
    nanu.penup()
    nanu.forward(10)
    nanu.pendown()
screen = Screen()
screen.exitonclick()

