# Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
length_of_chosen_word = len(chosen_word)
display.extend(length_of_chosen_word * "_")
print(display)

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
dead = 0
last_guess = ""
element = "_"
while element in display and dead < 5:
    if dead < 5:
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
        print(display)
    last_guess = guess
if element in display and dead >= 5:
    print("\nYou Lost!!!")
elif dead < 5:
    print("\nYou Won!!!")
