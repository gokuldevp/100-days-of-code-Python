import tkinter as tk
from random import choice
from datetime import datetime

# getting the list of of random words from text.txt
with open("text.txt", mode="r") as text:
    text_list = text.read().split("\n")


class TypingSpeedTestApp(tk.Frame):
    """Class to create Typing Speed Test App"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Typing Speed Test App")

        # setting screen size
        self.master.minsize(600, 600)
        self.master.maxsize(600, 600)

        # Alpha or Numeric Variables
        self.number_of_word = 0
        self.time = 0
        self.start_time = None
        self.end_time = None
        self.sample_text = None

        # Entry Variable
        self.entry = tk.Entry(font=("Times New Roman", 14), width=65)

        # Labels
        self.app_label = tk.Label(text="Typing Speed Test App", font=("Times New Roman", 30))
        self.score_label = tk.Label(text=f"High Score: {self.time}", font=("Times New Roman", 22))

        # Message
        self.text_message = tk.Message(justify="left", text=self.sample_text, font=("Times New Roman", 18))

        # Button
        self.start_button = tk.Button(text="Start Typing Test", command=self.start_text, font=("Times New Roman", 30))
        self.check_button = tk.Button(text="Check Typing Test", command=self.check_text, font=("Times New Roman", 15))

        # Widget Placement
        self.app_label.place(relx=.23, rely=.2)
        self.start_button.place(relx=.26, rely=0.5)

    def start_text(self):
        """Function to Start the Typing Speed Test"""
        # removing message widget
        self.text_message.place(relx=10, rely=10)

        # Remove entry and score widget
        self.score_label.place(relx=10, rely=10)
        self.entry.place(relx=10, rely=10)

        # Entry
        self.entry = tk.Entry(font=("Times New Roman", 14), width=65)

        # get start time
        self.start_time = datetime.now()

        # Get sample text
        self.get_sample_text()

        # Message
        self.text_message = tk.Message(justify="left", text=self.sample_text, font=("Times New Roman", 18))

        # reset Test
        self.start_button.config(text="Restart",command=self.start_text, font=("Times New Roman", 15))

        # Widget Placement
        self.app_label.place(relx=10, rely=10)
        self.start_button.place(relx=.13, rely=.9)
        self.check_button.place(relx=.63, rely=.9)
        self.text_message.place(relx=0, rely=0)
        self.entry.place(relx=0.01, rely=.8)

    def check_text(self):
        """Function to Check the result and show the Results"""
        # get end time
        self.end_time = datetime.now()

        wrong_words = 0
        right_words = 0

        # list of message words and typed words
        message_words = self.sample_text.split()
        typed_words = self.entry.get().split()

        # getting number of words
        if len(typed_words) <= 100:
            self.number_of_word = len(typed_words)
        else:
            self.number_of_word = 100

        # getting count of wrong words and right words
        for i in range(self.number_of_word):
            if message_words[i] == typed_words[i]:
                right_words += 1
            else:
                wrong_words += 1

        # calculating typing speed, wrong words and right words per minutes
        self.time = [float(num) for num in str(self.end_time - self.start_time).split(":")[1:]]
        wrong_speed = round(wrong_words/round(self.time[0] + self.time[1]/60, 2), 2)
        right_speed = round(right_words/round(self.time[0] + self.time[1]/60, 2), 2)
        speed = round(self.number_of_word/round(self.time[0] + self.time[1]/60, 2), 2)

        # showing the result
        score_text = f"Right Words  : {right_words}\n\nWrong Words: {wrong_words}\n\nTyping Speed: {speed} Words per Minutes\n\nWrong Speed: {wrong_speed} Words per Minutes\n\nRight Speed  : {right_speed} Words per Minutes"
        self.score_label.config(justify="left", text=score_text)

        # Start Again Button
        self.start_button.config(text="Start Again", font=("Times New Roman", 30))

        # Widget Placement
        self.score_label.place(relx=.20, rely=0.1)
        self.start_button.place(relx=.34, rely=0.8)
        self.text_message.place(relx=10, rely=10)
        self.check_button.place(relx=10, rely=10)
        self.entry.place(relx=10, rely=10)

    def get_sample_text(self):
        """Function to get Sample text"""
        self.sample_text = ""
        for i in range(100):
            self.sample_text += choice(text_list) + " "


root = tk.Tk()
app = TypingSpeedTestApp(root)
app.mainloop()
