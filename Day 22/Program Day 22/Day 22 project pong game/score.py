from turtle import Turtle


# creating class scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        """Creating class scoreboard"""
        super().__init__()
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.board()

    def board(self):
        """creating board to show the score"""
        self.clear()
        self.color("blue")
        self.goto(-100, 270)
        self.write(arg=f"Score:{self.left_score}", align="Center", font=("Times new roman", 18, "normal"))
        self.color("red")
        self.goto(100, 270)
        self.write(arg=f"Score:{self.right_score}", align="Center", font=("Times new roman", 18, "normal"))

    def left_update(self):
        """Increase left player score by 1 and show in the screen"""
        self.left_score += 1
        self.board()

    def right_update(self):
        """Increase right player score by 1 and show in the screen"""
        self.right_score += 1
        self.board()

    def check_winner(self):
        """Check winner and print the result"""
        self.color("white")
        self.goto(0, 0)
        if self.left_score > self.right_score:
            self.write(arg=f"Player Blue Won!", align="Center", font=("Times new roman", 20, "normal"))
        else:
            self.write(arg=f"Player Red Won!", align="Center", font=("Times new roman", 20, "normal"))
        self.goto(0, -100)
        self.write(arg=f"\nGame Over!", align="Center", font=("Times new roman", 20, "normal"))
