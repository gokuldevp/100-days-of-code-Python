#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

print("Welcome To The online Head or Tail Game!!!\n")
players = input("please select number of players?  \n\n")
if players == "1":
  players = int(players)
  if players == 1:
    player1 = input("\nPlease select Head or Tail?\n\n")
    player1 = player1.lower()
    result = random.randint(0,1)
    if result == 1:
      print("\nThe outcome is Head!\n")
    elif result == 0:
      print("\nThe outcome is Tail!\n")
    if (player1 == "head" and result == 1) or (player1 == "tail" and result == 0):
      print("You Won!")
    elif (player1 == "tail" and result == 1) or (player1 == "head" and result == 0):
      print("You Lost!")
    else:
      print("You havn't selected Head nor Tails!\nYou Lost!")
else:
  print("The game is only for Single player! \n\nSo please input 1 in number of players and try again.")
