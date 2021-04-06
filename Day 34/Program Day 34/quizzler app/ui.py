from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TRUE_IMAGE_PATH = "images/true.png"
FALSE_IMAGE_PATH = "images/false.png"
FONT = ("Times New Roman", 15, "bold")
CANVAS_FONT = ("Arial", 20, "italic")


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QUIZZER")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.que_text = self.canvas.create_text(150, 125, width=250, text="hello", font=CANVAS_FONT)

        self.canvas.grid(column=0, row=2, columnspan=2, pady=50)

        self.label = Label(text=f"Score: {self.quiz.score}", font=FONT, bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)

        self.true_image = PhotoImage(file=TRUE_IMAGE_PATH)
        self.true_button = Button(
            width=80,
            height=80,
            image=self.true_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.true_pressed
        )
        self.true_button.grid(column=0, row=3)
        self.false_image = PhotoImage(file=FALSE_IMAGE_PATH)
        self.false_button = Button(
            width=80,
            height=80,
            image=self.false_image,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.false_pressed
        )
        self.false_button.grid(column=1, row=3)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.que_text, text=question_text)
            self.label.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="active")
            self.false_button.config(state="active")
        else:
            self.canvas.itemconfig(self.que_text, text=f"The quiz is over your final score is: {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(1000, self.next_question)
