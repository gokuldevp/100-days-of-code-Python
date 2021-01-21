# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
length_of_chosen_word = len(chosen_word)
display.extend(length_of_chosen_word * "_")
print(str(display))
guess = input("Guess a letter: ").lower()

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

i = 0
for letter in chosen_word:
    if letter == guess:
        display[i] = guess
        i += 1
    else:
        i += 1

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".


print(display)
