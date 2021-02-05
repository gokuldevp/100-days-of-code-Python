from turtle import Turtle
X = 300
Y = 300


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(X, Y)
        self.pendown()
        self.width(20)
        self.color("red")

    def create_wall(self):
        self.goto(-X, Y)
        self.goto(-X, -Y)
        self.goto(X, -Y)
        self.goto(X, Y)
