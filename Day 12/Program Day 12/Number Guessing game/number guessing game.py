import random
from numberart import logo


def select_mode():
    if mode == "easy":
        print("\nYou selected Easy.")
        attempt_left = 20
    elif mode == "medium":
        print("\nYou selected Medium.")
        attempt_left = 10
    elif mode == "hard":
        print("\nYou selected Hard.")
        attempt_left = 5
    else:
        print("\nSince you selected a invalid mode, You are taken to default mode Easy.")
        attempt_left = 20

    return attempt_left


number = random.randint(1, 100)


def play():
    global mode, guess_number
    print(logo)
    print("\nWelcome to the Number Guessing game!")
    print("\nI am Guessing a number between 1 to 100")
    mode = input("\nSelect the mode to play ? 'Easy','Medium' or 'Hard' : ").lower()
    attempt_left = select_mode()
    while attempt_left > 0:
        print(f"\nYou have {attempt_left} attempt left:")
        guess_number = int(input("\nGuess a number : "))
        if guess_number == number:
            attempt_left = 0
        else:
            attempt_left -= 1
            if guess_number > number:
                print("\nYour number is Too high!")
            if guess_number < number:
                print("\nYour number is Too Low!")

    if guess_number == number:
        print("\nYou Guess the Right Number in!\nYou Won!")
    else:
        print("\nYou are out of attempts left!\nYou Lost!")


play()
play_again = True
while play_again:
    again = input("\nDo you want to play again? 'yes' or 'no' ").lower()
    if again == "yes":
        play()
    else:
        print("\nCome to play again!")
        play_again = False
