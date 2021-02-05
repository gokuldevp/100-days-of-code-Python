from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for part in range(3):
            self.add_segment(part)

    def add_segment(self, part):
        segment = Turtle("square")
        segment.penup()
        segment.color("blue")
        segment.speed("fastest")
        segment.goto(STARTING_POSITIONS[part])
        self.segments.append(segment)

    def grow(self):
        self.add_segment(-1)

    def move(self):
        for elements in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[elements - 1].xcor()
            new_y = self.segments[elements - 1].ycor()
            self.segments[elements].goto(x=new_x, y=new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
