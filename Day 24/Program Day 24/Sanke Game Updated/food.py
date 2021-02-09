from turtle import Turtle
import random


# creating class food
class Food(Turtle):
    def __init__(self):
        """creating food"""
        super().__init__()
        self.color("green")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.move()

    def move(self):
        """random movement of food"""
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)

