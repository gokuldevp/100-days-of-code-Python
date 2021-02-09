from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score import Scoreboard
from wall import Wall


def off():
    global game_is_on
    game_is_on = False


AXIS = 280

# Creating and setting up screen
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(width=610, height=610)

# creating wall
wall = Wall()
wall.create_wall()

# creating wall
snake = Snake()

# creating food
food = Food()

# creating scoreboard
scoreboard = Scoreboard()
screen.listen()

# setting up key press
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Left")
screen.onkey(fun=snake.left, key="Right")

# starting game
game_is_on = True
while game_is_on:
    screen.update()
    sleep(.1)
    snake.move()

    # setting conduction for snake to eat food
    if snake.head.distance(food) < 15:
        food.move()
        snake.grow()
        scoreboard.eat()

    # setting conduction for snake to byte tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.final()
            snake.reset()

    # setting conduction for snake to hit wall
    if snake.head.xcor() > AXIS or snake.head.xcor() < -AXIS or snake.head.ycor() > AXIS or snake.head.ycor() < -AXIS:
        scoreboard.final()
        snake.reset()

    # setting key to stop the game
    screen.onkey(key="s", fun=off)

screen.exitonclick()
