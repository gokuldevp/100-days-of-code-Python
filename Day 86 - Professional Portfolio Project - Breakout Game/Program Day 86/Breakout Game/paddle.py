from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x=0, y=-370, color="White"):
        """Initializing paddles and creating class paddles"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=.5, stretch_len=4)
        self.goto(x, y)

    def move_right(self):
        """move the paddle right"""
        if self.xcor() <= 340:
            self.forward(10)

    def move_left(self):
        """move the paddle left"""
        if self.xcor() >= -340:
            self.back(10)
