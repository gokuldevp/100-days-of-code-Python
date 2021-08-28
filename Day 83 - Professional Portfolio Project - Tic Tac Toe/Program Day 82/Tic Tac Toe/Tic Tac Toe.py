# directory of board
board = {"1": " ", "2": " ", "3": " ",
         "4": " ", "5": " ", "6": " ",
         "7": " ", "8": " ", "9": " "}

# key of valid number
valid_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def play_game():
    """function to start a play game."""

    new_game = input("Start a New Tic Tac Toe game?(yes or no) ")

    def full_board():
        """function to print board."""
        print(board["1"] + "|" + board["2"] + "|" + board["3"])
        print("-+-+-")
        print(board["4"] + "|" + board["5"] + "|" + board["6"])
        print("-+-+-")
        print(board["7"] + "|" + board["8"] + "|" + board["9"])

    def play(player):
        """function to play game."""
        full_board()
        select_num = input(f"\nPlayer {player} turn select number {valid_list} :")
        if select_num in valid_list:
            valid_list.remove(select_num)
            if player == "X":
                board[select_num] = "X"
            elif player == "O":
                board[select_num] = "O"
        else:
            print(f"\nUse number {valid_list}")
            play(player)

    def check_result(player):
        """function to check which player won of if game is a draw."""
        if board["1"] == board["2"] == board["3"] == player or board["4"] == board["5"] == board["6"] == player or board["7"] == board["8"] == board["9"] == player or board["1"] == board["5"] == board["9"] == player or board["3"] == board["5"] == board["7"] == player or board["1"] == board["4"] == board["7"] == player or board["2"] == board["5"] == board["8"] == player or board["3"] == board["6"] == board["9"] == player:
            print(f"Player {player} Won!!!\n ")
            return True
        elif len(valid_list) == 0:
            print(f"Game is a Draw!\n ")
            return True

    # if statement to decide to play game according to player decision
    if new_game.lower() == "yes":
        start_game = True
    else:
        start_game = False
        print("Have a nice Day :)")

    # while function to play game between player X and O
    while start_game:
        for player_name in ["X", "O"]:
            play(player_name)
            if check_result(player_name):
                start_game = False
                full_board()
                break


play_game()
