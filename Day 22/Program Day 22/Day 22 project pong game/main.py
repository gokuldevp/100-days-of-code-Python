from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

X_COR = 405

# Creating and setting up screen
screen = Screen()
screen.title("The Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

# creating left and right side
line = Turtle()
line.goto(0, 300)
line.color("white")
line.hideturtle()
line.goto(0, -300)

# creating paddles
paddle1 = Paddle(x=370, y=0, color="red")
paddle2 = Paddle(x=-380, y=0, color="blue")

# creating Scoreboard
scoreboard = Scoreboard()


# setting up keys for paddles movement
screen.onkeypress(key="Up", fun=paddle1.move_up)
screen.onkeypress(key="Down", fun=paddle1.move_down)
screen.onkeypress(key="w", fun=paddle2.move_up)
screen.onkeypress(key="s", fun=paddle2.move_down)

game_is_on = True
while game_is_on:
    # creating ball
    ball = Ball()
    ball.start_direction()
    # screen.update()
    round_start = True
    while round_start:
        speed = 0
        screen.update()
        ball.move()
        time.sleep(.01)

        # creating conduction to update score
        if ball.xcor() > X_COR or ball.xcor() < -X_COR:
            if ball.xcor() > 400:
                scoreboard.left_update()
            elif ball.xcor() < -400:
                scoreboard.right_update()
            round_start = False

        # bouncing of the ball from paddles
        elif ball.distance(paddle1) < 30 and ball.xcor() > 360 or ball.distance(paddle2) < 30 and ball.xcor() < -370:
            ball.setheading(ball.heading()+100)
            ball.forward(3)

        # checking the winner
        if scoreboard.left_score == 10 or scoreboard.right_score == 10:
            game_is_on = False
            scoreboard.check_winner()


screen.exitonclick()
