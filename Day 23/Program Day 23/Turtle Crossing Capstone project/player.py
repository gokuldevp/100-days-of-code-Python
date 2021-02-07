from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# creating class Player
class Player(Turtle):
    def __init__(self):
        """initializing turtle properties"""
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.refresh_count = 0

    def move(self):
        """moving turtle up"""
        self.forward(MOVE_DISTANCE)

    def refresh(self):
        """refreshing turtle when it reaches finishing line"""
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.refresh_count += 1
