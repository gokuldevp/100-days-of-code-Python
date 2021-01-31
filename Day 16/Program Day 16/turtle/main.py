# from turtle import Turtle, Screen
#
#
# gokul = Turtle()
# print(gokul)
# gokul.shape("turtle")
# gokul.color("red")
# gokul.forward(100)
# gokul.color("green")
# gokul.circle(10,100, 90)
# gokul.color("blue")
# gokul.circle(10, 90)
# gokul.color("yellow")
# gokul.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

