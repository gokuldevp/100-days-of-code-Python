import random
from art import vs
from art import logo
from game_data import data


def person():
    global person_data
    length_of_data = len(data)
    num = random.randint(0,length_of_data-1)
    person_data = data[num]["name"]+", "+data[num]["description"]+", "+data[num]["country"]
    followers = data[num]["follower_count"]
    return followers


play_again = True
while play_again:
    score = 0
    follower_a = person()
    person_a = person_data
    play = True
    while play:
        print(logo)
        follower_b = person()
        person_b = person_data
        while person_b == person_a:
            follower_b = person()
            person_b =person_data
        print(f"\nPerson A: {person_a}.")
        print(vs)
        print(f"\nPerson B: {person_b}.")
        guess = input("\nWho do you think have more Follower on instagram? Type 'A' or 'B' : ").lower()
        if guess == "a":
            if follower_a > follower_b:
                score += 1
                print(f"\nYou are Right! Your Total score = {score}")
            elif follower_b > follower_a:
                print(f"\nYou are Wrong! Your Total score = {score}")
                play = False
        elif guess == "b":
            if follower_b > follower_a:
                score += 1
                print(f"\nYou are Right! Your Total score is {score}")
            elif follower_a >follower_b:
                print(f"\nYou are Wrong! Your Total score is {score}")
                play = False
        else:
            print(f"\nYou didn't Made a guess! Your Total scor is {score}")
            play = False
        follower_a = follower_b
        person_a = person_b
    you_play_again = input("\nDo You want to play again? Type 'Yes' or 'No' : ").lower()
    if you_play_again == "yes":
        pass
    else:
        print("\nCome again Later!")
        play_again = False
