import time
import random
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
import car_manager
from scoreboard import Scoreboard

# create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# creating the player
turtle = Player()

# creating score board
score = Scoreboard()

# creating list of cars
car_list = []

# setting up press keys for turtle control
screen.onkeypress(key="Up", fun=turtle.move)

count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    old_turtle = turtle.refresh_count

    # creating cars
    if count % 6 == 0:
        for car in range(random.randint(0, 5)):
            new_car = CarManager()
            car_list.append(new_car)

    # operating cars
    for car in range(len(car_list)):
        car_list[car].move()
        car_list[car].refresh()

        # finding if car cross finishing line
        if turtle.ycor() > FINISH_LINE_Y and car_manager.STARTING_MOVE_DISTANCE <= car_manager.MOVE_INCREMENT:
            car_manager.STARTING_MOVE_DISTANCE += 1

        # conduction for game over
        if turtle.distance(car_list[car]) < 20:
            score.game_over()
            game_is_on = False

    turtle.refresh()

    # leveling up game
    if turtle.refresh_count > old_turtle:
        score.level_up()
    count += 1
screen.exitonclick()
