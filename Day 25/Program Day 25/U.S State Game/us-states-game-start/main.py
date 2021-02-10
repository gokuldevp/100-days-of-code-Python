# importing libraries
import turtle
import pandas as pd

# initializing path and opening the csv file
PATH = "50_states.csv"
STATE_DF = pd.read_csv(PATH)
STATE_SEC = STATE_DF["state"]


def check_input_state_is_correct():
    """Check the input of the player and write the name of the state's in map according to input, if player write stop
    end the game."""
    global play_again, play, correct
    if guess_state in states_list:
        states_list.remove(guess_state)
        current_state_row = STATE_DF[STATE_SEC == guess_state]
        x_pos = int(current_state_row.x)
        y_pos = int(current_state_row.y)
        answer.goto(x_pos, y_pos)
        answer.write(f"{guess_state}", font=("Times New Roman", 8, "normal"))
        correct = True
    elif guess_state == "Stop":
        play = screen.textinput(title="Play again",
                                prompt="Look's like you stop the game.\nDo you like to play again?'Yes' or 'No' ?").title()
        play_again = False
        correct = False
    else:
        correct = False

    def check_player_won():
        """check if player won?"""
        global play_again, play
        if len(states_list) < 1:
            play_again = False
            play = screen.textinput(title="Play again",
                                    prompt="Look's like you guess all states correctly!\nDo you like to play again?'Yes' or 'No' ?").title()

    check_player_won()


correct = False
play = "Yes"
game_is_on = True

# starting the game
while game_is_on:
    score = 0

    # creating the screen and setting up the screen
    screen = turtle.Screen()
    screen.setup(width=725, height=490)
    screen.title("U.S.State Game")

    # setting up the screen image
    IMAGE = "blank_states_img.gif"
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)

    # creating turtle name answer to write the name of states on the screen
    answer = turtle.Turtle()
    answer.hideturtle()
    answer.penup()

    # creating turtle to write the score on screen
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.goto(-200, 200)
    score_turtle.write(f"score: {score}", font=("Times New Roman", 15, "normal"))

    # creating the list of states from csv file
    states_list = STATE_SEC.to_list()
    play_again = True
    while play_again:
        # getting players guess input
        guess_state = screen.textinput(title="Guess the state", prompt="Write the state's name ?").title()

        # check players input
        check_input_state_is_correct()

        # conduction for increment score
        if correct:
            score += 1
            score_turtle.clear()
            score_turtle.write(f"score: {score}", font=("Times New Roman", 15, "normal"))
    if play == "Yes":
        screen.clear()
    else:
        game_is_on = False
        screen.exitonclick()
