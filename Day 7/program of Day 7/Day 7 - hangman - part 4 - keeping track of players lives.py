# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []
length_of_chosen_word = len(chosen_word)
display.extend(length_of_chosen_word * "_")
list_join = " "
print(f"{list_join.join(display)}")

dead = 0
last_guess = ""
element = "_"
while element in display and dead < 6:
    hangman = stages[6-dead]
    print(hangman)
    if dead < 6:
        guess = input("\nGuess a letter: \n").lower()
        if guess == last_guess:
            print("\nLetter repeated!!!\n")
            dead += 1
        else:
            i = 0
            if guess in chosen_word:
                for letter in chosen_word:
                    if letter == guess:
                        display[i] = guess
                        i += 1
                    else:
                        i += 1
                print("\nCorrect letter!!!\n")
            else:
                print("\nWrong letter!!!\n")
                dead += 1
        print(f"{list_join.join(display)}")
    last_guess = guess
if element in display and dead >= 6:
    hangman = stages[6-dead]
    print(hangman)
    print("\nHangman Dies!\n\nYou Lost!!!")
elif dead < 6:
    print("\nYou Saved the Hangman!\n\nYou Won!!!")
print("\n***GAME OVER***")
