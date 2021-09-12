from turtle import Turtle


class Target(Turtle):
    def __init__(self, x, y, color):
        """Class to creating Target"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(9999999999999999999999)
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.goto(x, y)
        self.color(color)

    def remove_target(self):
        self.goto(1000, 1000)

