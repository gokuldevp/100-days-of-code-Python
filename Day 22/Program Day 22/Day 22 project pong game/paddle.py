from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y, color):
        """Initializing paddles and creating class paddles"""
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(90)
        self.color(color)
        self.shapesize(stretch_wid=.5, stretch_len=3)
        self.goto(x, y)

    def move_up(self):
        """move the paddle up"""
        if self.ycor() <= 240:
            self.forward(20)

    def move_down(self):
        """move the paddle down"""
        if self.ycor() >= -240:
            self.back(20)



