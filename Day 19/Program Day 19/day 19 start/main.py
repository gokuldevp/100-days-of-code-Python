from turtle import Screen, Turtle

aju = Turtle()
screen = Screen()


def move():
    aju.color("red")
    aju.forward(10)


def right():
    aju.right(45)


def left():
    aju.left(45)


def back():
    aju.color("blue")
    aju.back(10)


aju.width(20)
screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="s", fun=back)
screen.exitonclick()
