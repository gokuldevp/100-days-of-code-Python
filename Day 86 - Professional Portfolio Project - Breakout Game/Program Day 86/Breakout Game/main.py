# Imports
from turtle import Screen
from paddle import Paddle
from score import Scoreboard
from ball import Ball
from brick import create_walls
from target import Target
from random import choice

# Try and catch to get any errors
try:
    # list of color for target
    colors = ["Red", "Blue", "Green", "Orange", "Brown", "Indigo", "Silver"]

    # Creating and Config Screen
    screen = Screen()
    screen.title("Breakout Game")
    screen.bgcolor("Black")
    screen.setup(800, 800)
    screen.listen()

    # Creating walls
    create_walls()

    # Creating Paddle
    paddle = Paddle()
    paddle.showturtle()

    # Creating Scoreboard
    score = Scoreboard()

    # Creating Walls
    ball = Ball(paddle.xcor())
    ball.showturtle()

    # Creating movement of Paddle to left and right based on Left and Right keys
    screen.onkeypress(key="Left", fun=paddle.move_left)
    screen.onkeypress(key="Right", fun=paddle.move_right)

    # Starting Game
    while True:

        # Creating Targets
        target = {}
        for i in range(-350, 360, 50):
            for j in range(-200, 350, 50):
                target[f"{i, j}"] = Target(x=i, y=j, color=choice(colors))
                target[f"{i, j}"].showturtle()

        # Setting Ball Heading Direction
        ball.start_direction()
        ball.move()

        # Starting Round
        round_start = True
        while round_start:

            # bouncing ball back when it hit the Paddle
            if paddle.distance(ball) < 40 and ball.ycor() < paddle.ycor() + 10:
                ball.setheading(- ball.heading())

            # bouncing ball back when it hit the Target, Increase Score, Remove Target that the ball touch
            for i in range(-350, 360, 50):
                for j in range(-200, 350, 50):
                    if target[f"{i, j}"].distance(ball) < 40:
                        target[f"{i, j}"].remove_target()
                        ball.setheading(- ball.heading())
                        score.score_update()

            # Start Game from Start When the Game is over
            if ball.ycor() <= -410:
                score.score = 0  # reset score
                ball.start_direction()
                ball.goto(paddle.xcor(), -360)  # Setting Initial position of ball

                # Removing all target
                for i in range(-350, 360, 50):
                    for j in range(-200, 350, 50):
                        target[f"{i, j}"].remove_target()
                # Update Scoreboard
                score.board()
                break

            # Update screen and move ball
            screen.update()
            ball.move()
except:
    pass
