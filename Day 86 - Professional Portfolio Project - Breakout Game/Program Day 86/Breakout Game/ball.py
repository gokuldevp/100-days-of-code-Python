from turtle import Turtle
import random
Y_COR = 380


class Ball(Turtle):
    def __init__(self, x):
        """Initializing class ball and Creating class Ball"""
        super().__init__()
        self.hideturtle()
        self.goto(x, -360)
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.speed(100)
        self.shapesize(stretch_wid=.5, stretch_len=.5)

    def start_direction(self):
        """setting starting direction"""
        self.setheading(random.randint(20, 160))

    def move(self):
        """movement of the ball"""

        # bouncing ball back when it hit the wall
        if self.ycor() >= Y_COR:
            self.setheading(-self.heading())
            self.forward(10)
        elif self.xcor() >= Y_COR or self.xcor() <= -Y_COR:
            self.setheading((180-self.heading()))
            self.forward(5)

        # move when not hit any wall
        else:
            self.forward(5)
