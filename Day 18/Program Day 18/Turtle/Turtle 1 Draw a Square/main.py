from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
colour = ["red", "green", "Blue", "yellow"]
for move in range(4):
    turtle.color(colour[move])
    turtle.forward(100)
    turtle.right(90)
for move in range(4):
    turtle.color(colour[move])
    turtle.forward(100)
    turtle.left(90)
for move in range(4):
    turtle.color(colour[move])
    turtle.back(100)
    turtle.right(90)
for move in range(4):
    turtle.color(colour[move])
    turtle.back(100)
    turtle.left(90)
















screen = Screen()
screen.exitonclick()
