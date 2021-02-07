from turtle import Turtle

FONT = ("Courier", 24, "normal")


# creating the score board
class Scoreboard(Turtle):
    """initializing the scoreboard"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-200, 240)
        self.hideturtle()
        self.level = 1
        self.show_level()

    def show_level(self):
        """Showing level on screen"""
        self.write(f"level = {self.level}", align="Center", font=FONT)

    def level_up(self):
        """increase level on set conduction """
        self.level += 1
        self.clear()
        self.show_level()

    def game_over(self):
        """Writing game over!"""
        self.goto(0, 0)
        self.write("Game Over!", align="Center", font=FONT)
