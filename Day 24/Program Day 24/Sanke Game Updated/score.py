from turtle import Turtle
ALIGNMENT = "right"
FONT = ("Times New Roman", 13, "normal")


# creating class Scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        """this class create scoreboard"""
        super().__init__()
        self.score = 0

        # opening data.txt for reading
        with open("Data.txt") as file_read:
            self.high_score = int(file_read.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(80, 287)
        self.update_score()

    def update_score(self):
        """function for updating scoreboard"""
        self.clear()
        self.write(f"The score: {self.score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def final(self):
        """function for finishing the current game"""
        if self.score > self.high_score:
            self.high_score = self.score

            # write the score to a txt document so that we can get the high score when we start a new game
            with open("Data.txt", mode="w") as file_write:
                file_write.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def eat(self):
        """function used when snake eats the food"""
        self.score += 1
        self.update_score()


