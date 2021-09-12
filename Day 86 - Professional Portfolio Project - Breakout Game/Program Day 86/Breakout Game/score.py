from turtle import Turtle

# getting high score from score.txt
with open("score.txt") as high_score:
    new_high_score = int(high_score.read())


# creating class scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        """Creating class scoreboard"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = new_high_score
        self.board()

    def board(self):
        """creating board to show the score"""
        self.clear()
        self.color("White")
        self.goto(-20, 360)
        self.write(arg=f"Score:{self.score}     High Score:{self.high_score}", align="Center", font=("Times new roman", 18, "normal"))

    def score_update(self):
        """Increase player score by 1, Update High Score if score is higher and show in the screen"""
        self.score += 1
        if self.high_score < self.score:
            self.high_score = self.score
            with open("score.txt", "w") as update_score:
                update_score.write(str(self.high_score))
        self.board()
