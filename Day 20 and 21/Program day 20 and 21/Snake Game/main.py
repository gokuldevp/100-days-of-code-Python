from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score import Scoreboard
from wall import Wall

AXIS = 280
screen = Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(width=610, height=610)
screen.tracer(0)

wall = Wall()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
wall.create_wall()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Left")
screen.onkey(fun=snake.left, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.move()
        snake.grow()
        scoreboard.eat()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.final()

    if snake.head.xcor() > AXIS or snake.head.xcor() < -AXIS or snake.head.ycor() > AXIS or snake.head.ycor() < -AXIS:
        scoreboard.final()
        game_is_on = False


screen.exitonclick()
