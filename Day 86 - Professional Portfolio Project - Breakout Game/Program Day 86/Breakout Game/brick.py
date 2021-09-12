from turtle import Turtle


class Brick(Turtle):
    def __init__(self, x, y, width, length, color="Gold"):
        """Initializing paddles and creating class paddles"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=width, stretch_len=length)
        self.goto(x, y)


def create_walls():
    """Creating walls on Three sides"""
    brick1 = Brick(0, 395, .8, 40)
    brick2 = Brick(390, 0, 40, .5)
    brick3 = Brick(-395, 0, 40, .8)
    brick1.showturtle()
    brick2.showturtle()
    brick3.showturtle()
