from turtle import Screen, Turtle


gok = Turtle()
screen = Screen()


def forward():
    gok.forward(1)


def backward():
    gok.back(1)


def right():
    gok.right(10)


def left():
    gok.left(10)


def clear():
    gok.clear()
    gok.penup()
    gok.home()
    gok.pendown()


screen.listen()
screen.onkeypress(key="w", fun=forward)
screen.onkeypress(key="s", fun=backward)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
