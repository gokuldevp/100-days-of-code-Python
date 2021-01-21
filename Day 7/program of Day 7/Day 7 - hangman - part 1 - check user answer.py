# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

list_length = len(word_list)
word = random.randint(0, list_length-1)
chosen_word = word_list[word]
word_length = len(chosen_word)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Choose a letter? ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
i = 0
for n in range(0, word_length):
    if guess == chosen_word[i]:
        a = print("Right")
        i += 1
    elif guess != chosen_word[i]:
        b = print("wrong ")
        i += 1

