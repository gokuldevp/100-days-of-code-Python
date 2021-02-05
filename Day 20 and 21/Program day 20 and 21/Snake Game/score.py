from turtle import Turtle
ALIGNMENT = "right"
FONT = ("Times New Roman", 13, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(30, 287)
        self.eat()

    def final(self):
        self.goto(30, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def eat(self):
        self.clear()
        self.write(f"The score is : {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1
