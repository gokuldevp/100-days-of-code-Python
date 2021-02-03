from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def start(turtle, y, pos):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x=-230, y=y)
    turtle.color(colors[pos])
    turtle.showturtle()


def race():
    red.forward(red_distance)
    orange.forward(orange_distance)
    yellow.forward(yellow_distance)
    green.forward(green_distance)
    blue.forward(blue_distance)
    purple.forward(purple_distance)


def total_distance():
    global red_total_distance, orange_total_distance, yellow_total_distance, green_total_distance, blue_total_distance, purple_total_distance
    red_total_distance += red_distance
    orange_total_distance += orange_distance
    yellow_total_distance += yellow_distance
    green_total_distance += green_distance
    blue_total_distance += blue_distance
    purple_total_distance += purple_distance
    return max(red_total_distance, orange_total_distance, yellow_total_distance, green_total_distance, blue_total_distance, purple_total_distance)


def check_winner():
    if max(red_total_distance, orange_total_distance, yellow_total_distance, green_total_distance, blue_total_distance, purple_total_distance) == red_total_distance:
        return "red"
    elif max(red_total_distance, orange_total_distance, yellow_total_distance, green_total_distance, blue_total_distance, purple_total_distance) == orange_total_distance:
        return "orange"
    elif max(red_total_distance, orange_total_distance, yellow_total_distance, green_total_distance, blue_total_distance, purple_total_distance) == yellow_total_distance:
        return "yellow"
    elif max(red_total_distance, orange_total_distance, yellow_total_distance, green_total_distance, blue_total_distance, purple_total_distance) == green_total_distance:
        return "green"
    elif max(red_total_distance, orange_total_distance, yellow_total_distance, green_total_distance, blue_total_distance, purple_total_distance) == blue_total_distance:
        return "blue"
    elif max(red_total_distance, orange_total_distance, yellow_total_distance, green_total_distance, blue_total_distance, purple_total_distance) == purple_total_distance:
        return "purple"


total_dis = 0
red_total_distance = 0
orange_total_distance = 0
yellow_total_distance = 0
green_total_distance = 0
blue_total_distance = 0
purple_total_distance = 0
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color = ",".join(colors)
user_bit = screen.textinput(title="Bit on Turtle", prompt=f"Which turtle are you biting for? {color}? type a color :").lower()
red = Turtle(shape="turtle")
start(turtle=red, y=-125, pos=0)
orange = Turtle(shape="turtle")
start(turtle=orange, y=-75, pos=1)
yellow = Turtle(shape="turtle")
start(turtle=yellow, y=-25, pos=2)
green = Turtle(shape="turtle")
start(turtle=green, y=25, pos=3)
blue = Turtle(shape="turtle")
start(turtle=blue, y=75, pos=4)
purple = Turtle(shape="turtle")
start(turtle=purple, y=125, pos=5)
while total_dis < 450:
    red_distance = random.randint(0, 15)
    orange_distance = random.randint(0, 15)
    yellow_distance = random.randint(0, 15)
    green_distance = random.randint(0, 15)
    blue_distance = random.randint(0, 15)
    purple_distance = random.randint(0, 15)
    race()
    total_dis = total_distance()
winner = check_winner()
print(f"The winner of the race is turtle '{winner}'")
if user_bit == winner:
    print("\nYou won the bit!")
else:
    print("\nYou lost the bit!")
screen.exitonclick()
