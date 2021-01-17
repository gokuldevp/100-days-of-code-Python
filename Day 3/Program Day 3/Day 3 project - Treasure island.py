print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print("\n|   left   |   |    right    |\n|          |   |             |\n")
go = input("\nYou are at a crossroad, where would you like to go?\nPrint 'left' or 'right'? \n").lower()
if go == "left":
  lake = input("\nYou are at a lake.There is an island on the middke of the lake.What age you going to do?\nWait for a boat or swim to the island?\nPrint 'wait' or 'swim'? \n").lower()
  if lake == "wait":
    print("\n|   red   ||  blue   ||  yellow  |\n")
    door = input("\nYou reached the island! There you can see a house with Three doors. \nWhich door will you choose red,blue or yellow? \nPrint 'red','blue' or 'yellow'? \n").lower()
    if door == "yellow":
      print("\nYou Found a Golden Chest!\nYou Win!\n")
    elif door == 'red':
      print("\nYou are Eaten by a Lion!\nYou Died\nGame Over!")
    elif door == "blue":
      print("\nYou fell into a room of fire!\nYou Died!\nGame Over!")
    else:
      print("\nGame Over!")
  elif lake == "swim":
    print("\nAttacked by Sharks!\nYou Died!\nGame Over!")
  else:
    print("\nGame Over!")
elif go == "right":
  print("\nYou fall into a Hole!\nYou died!\nGame Over!")
else:
  print("Game Over!")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
