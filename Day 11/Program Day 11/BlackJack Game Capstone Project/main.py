import random
import blackjackart

# import os

Card_Dir = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "K": 10,
    "Q": 10,
}


def drawcard():
    """Draw a random card"""
    card = random.choices(list(Card_Dir))
    return card


def system_draw(player_stop, player_points, system_cards, player_cards):
    """Turn of System draw"""
    global system_points
    system_start = True
    while player_stop and system_start:
        # ace(system_cards, system_points)
        while system_points <= player_points or system_points <= 16:
            if system_points < 21:
                system_card_2 = drawcard()
                system_cards.extend(system_card_2)
                system_points = 0
                Card_Dir["A"] = 11
                if "A" in player_cards and player_points > 21:
                    Card_Dir["A"] = 1
                for system_card in system_cards:
                    system_points += Card_Dir["".join(system_card)]
                Card_Dir["A"] = 11
            system_start = False
        print(f"\nYour cards are : {player_cards}")
        print(f"\nPlayer Point : {player_points}")
        print(f"\nSystem cards are : {system_cards}")
        print(f"\nSystem Points : {system_points}")
        if system_points > 21:
            print("\nYou Won!")
            print("\nGameover!")
            startgame()
        elif 16 < system_points < 22:
            print("\nYou Lost!")
            print("\nGameover!")
            startgame()


# def ace(cards, points):
#     """Change card A value"""
#     if "A" in cards:
#         if points > 21:
#             points -= 10
#         else:
#             pass
#     return points



def startgame():
    """Start the game"""
    # os.system('cls')
    print(blackjackart.logo)
    count = 0
    global system_cards, player_cards, system_points, player_points
    can_we_start_game = input("\nCan we Start the Game? Type 'Yes' or 'No' : ").lower()
    if can_we_start_game == "yes":
        start_game = True
        again = True
        player_stop = False
        system_start = True
        player_points = 0
        system_points = 0
        while start_game:
            player_card_1 = drawcard()
            system_card_1 = drawcard()
            system_cards = system_card_1
            system_card_2 = ["?"]
            player_cards = player_card_1
            while again:
                if player_points < 21:
                    player_card_2 = drawcard()
                    player_cards.extend(player_card_2)

                print(f"\nYour cards are : {player_cards}")
                player_points = 0
                system_points = 0
                Card_Dir["A"] = 11
                if "A" in player_cards and player_points > 21:
                        Card_Dir["A"] = 1

                for player_card in player_cards:
                    player_points += Card_Dir["".join(player_card)]


                print(f"\nPlayer Point : {player_points}")
                Card_Dir["A"] = 11
                print(f"\nSystem cards are : {system_cards},{system_card_2}")
                for system_card in system_cards:
                    system_points += Card_Dir["".join(system_card)]

                    # count = 1
                print(f"\nSystem Points : {system_points}")
                # ace(player_cards, player_points)
                if player_points <= 21 and again:
                    if player_points < 21:
                        draw_again = input("\nDo you want to draw again? 'Yes' or 'No' : ").lower()
                        if draw_again == "yes":
                            again = True
                        elif draw_again == "no":
                            player_stop = True
                            again = False
                            system_draw(player_stop, player_points, system_cards, player_cards)
                    else:
                        again = False
                        player_stop = True
                        system_draw(player_stop, player_points, system_cards, player_cards)

                else:
                    again = False
                    print("\nYou Lost!")
                    print("\nGameover!")
                    startgame()
        system_draw(player_stop, player_points, system_cards, player_cards)
        start_game = False
    if can_we_start_game == "yes":
        if system_points <= 21 and player_points <= 21:
            if system_points > player_points:
                print("\nYou Won!")
        elif system_points < player_points:
            print("\nYou Lost!")
        else:
            print("\nIt is a draw!")
        print("\nGameover!")
        startgame()
    else:
        print("\nIf you don't like to play now You can always play next time!")


startgame()
