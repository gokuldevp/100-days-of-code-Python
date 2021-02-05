from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        # self.speed("fastest")
        self.shape("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.move()

    def move(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)

