# Step 5

import random
import hangman_art
import hangman_wordlist

chosen_word = random.choice(hangman_wordlist.word_list)

print("HELLO EVERYONE I AM GOKUL DEV.P AND WELCOME TO HANGMAN GAME !!!\n")
print(hangman_art.logo)
display = []
length_of_chosen_word = len(chosen_word)
display.extend(length_of_chosen_word * "_")
list_join = " "
print(f"{list_join.join(display)}")
dead = 0
last_guess = ""
element = "_"

while element in display and dead < 6:
    hangman = hangman_art.stages[6-dead]
    print(hangman)

    if dead < 6:
        guess = input("\nGuess a letter: \n").lower()

        if guess == last_guess:
            print(f"\nLetter {guess} is in the Word, But it's repeated!!!\nYou lost a life!!!\n")
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

                print(f"\nletter {guess} is in the Word!!!\nWell Done!!!\n")

            else:
                print(f"\nletter {guess} is not in the Word!!! \nYou lost a life!!!\n")
                dead += 1

        print(f"{list_join.join(display)}")

    last_guess = guess

if element in display and dead >= 6:
    hangman = hangman_art.stages[6-dead]
    print(hangman)
    print("\nYou lost all Life, Hangman Dies!!!\n\nYou Lost!!!")

elif dead < 6:
    print("\nYou Saved the Hangman!!!\n\nYou Won!!!")

print("\n***GAME OVER***")
