from turtle import Turtle
import random
Y_COR = 290


class Ball(Turtle):
    def __init__(self):
        """Initializing class ball and Creating class Ball"""
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)

    def start_direction(self):
        """setting starting direction"""
        self.setheading(random.choice([random.randint(290, 430), random.randint(110, 250)]))

    def move(self):
        """movement of the ball"""
        if self.ycor() >= Y_COR or self.ycor() <= -Y_COR:
            self.setheading(-self.heading())
            self.forward(3)
        else:
            self.forward(3)
