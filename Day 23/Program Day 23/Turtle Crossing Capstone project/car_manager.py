import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# creating class CarManager
class CarManager(Turtle):
    def __init__(self):
        """Initializing car properties"""
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=280, y=random.randint(-230, 230))
        self.refresh_count = 0

    def move(self):
        """moving car"""
        self.forward(STARTING_MOVE_DISTANCE)

    def refresh(self):
        """refresh car"""
        self.clear()


