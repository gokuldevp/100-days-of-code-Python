from tkinter import *
import pandas as pd
import random
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
CSV_FILE_PATH = "data/french_words.csv"
english_word = None
word_dict = None
# *********************************************************************************************************************#
data = pd.read_csv(CSV_FILE_PATH)
word_dict_list = data.to_dict("records")
unknown_card_df = word_dict_list


# ******************************************** change cards function **************************************************#
def change_card():
    """function to change cards"""

    global english_word, flip_timer, word_dict

    window.after_cancel(flip_timer)

    word_dict = random.choice(word_dict_list)
    french_word = word_dict["French"]
    english_word = word_dict["English"]

    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    canvas.itemconfig(canvas_image, image=FRONT_IMG)

    flip_timer = window.after(3000, flip_card)


# ********************************************** flip card function ***************************************************#
def flip_card():
    """function to flip cards"""
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=BACK_IMG)


# *********************************************** is known function ***************************************************#
def is_known():
    """function if word is unknown"""
    global unknown_card_df
    try:
        word_dict_list.remove(word_dict)
        unknown_cards_df = pd.DataFrame(word_dict_list)
        unknown_cards_df.to_csv("data/unknown_words.csv", index=False)
        change_card()
    except ValueError:
        messagebox.showwarning(title="Empty", message="You have no more words to learn in the directory")
    except IndexError:
        messagebox.showwarning(title="Empty", message="You have no more words to learn in the directory")


# ********************************************** unknown function *****************************************************#
def unknown():
    """function if word is known"""
    try:
        unknown_cards_df = pd.DataFrame(unknown_card_df)
        unknown_cards_df.to_csv("data/unknown_words.csv", index=False)
        change_card()
    except IndexError:
        messagebox.showwarning(title="Empty", message="You have no more words to learn in the directory")


# ************************************************ USER INTERFACE *****************************************************#

# window
window = Tk()
window.title("FLASH CARD")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card)

FRONT_IMG = PhotoImage(file="images/card_front.png")
BACK_IMG = PhotoImage(file="images/card_back.png")
RIGHT_IMG = PhotoImage(file="images/right.png")
WRONG_IMG = PhotoImage(file="images/wrong.png")

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
canvas.config(highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=FRONT_IMG)
language_text = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2, rowspan=6)

# button
right_button = Button(image=RIGHT_IMG, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=6)
wrong_button = Button(image=WRONG_IMG, highlightthickness=0, command=unknown)
wrong_button.grid(column=0, row=6)

change_card()
window.mainloop()
