import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock-paper-scissors online game!!!\n")

name = input("what is your name? ")
name = name.upper()
rock_paper_scissors = [rock,paper,scissors]
player = input(f"So {name}, \nWhat do you choose? \nRock, Paper or Scissors? \n")
player = player.lower()
your_result = "You don't select rock, paper or scissors!\n"
print(f"\n{name} :\n")
if player == "rock":
  your_result = rock
elif player == "paper":
  your_result = paper
elif player == "scissors":
  your_result = scissors
else:
  print("What did you jest choose? ")
print(your_result)
cpu = random.randint(0,2)
print("\nComputer :\n")
cpu_result = rock_paper_scissors[cpu]
print(cpu_result)
if your_result == cpu_result:
  print("No one Won!\nThe game is a Draw!!!")
elif (your_result == rock and cpu_result == scissors) or (your_result == scissors and cpu_result == paper) or (your_result == paper and cpu_result == rock):
  print("Cpu Lost!\nYou Won!!!")
elif (cpu_result == rock and your_result == scissors ) or (cpu_result == scissors and your_result == paper) or (cpu_result == paper and your_result == rock):
  print("Cpu Won!\nYou Lost!!!")
else:
  print("The result can't be determined...")

# OR

#import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# game_images = [rock, paper, scissors]
# choice = [0,1,2]
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice in choice:
#  print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0:
#   print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")
