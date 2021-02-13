from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
IMAGE = "tomato.png"

round_num = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global round_num
    window.after_cancel(timer)
    timer_label.config(text=" TIMER ", fg=GREEN)
    marks_label.config(text="")
    canvas.itemconfig(timer_change, text="00:00")
    round_num = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    def set_time():
        global round_num, time_in_sec

        if round_num == 8:
            timer_label.config(fg=RED, text=" BREAK ")
            time_in_sec = LONG_BREAK_MIN * 60

        elif round_num % 2 == 0:
            timer_label.config(fg=PINK, text=" BREAK ")
            time_in_sec = SHORT_BREAK_MIN * 60

        elif round_num % 2 != 0:
            timer_label.config(fg=GREEN, text=" WORK  ")
            time_in_sec = WORK_MIN * 60

        round_num += 1
        return time_in_sec

    count_down(set_time())


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minute = int(count/60)
    second = count % 60
    list_of_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    if second in list_of_num:
        second = f"0{second}"

    if minute in list_of_num:
        minute = f"0{minute}"

    canvas.itemconfig(timer_change, text=f"{minute}:{second}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        mark = ""

        for a in range(int(round_num/2)):
            mark += "✔"
            marks_label.config(text=mark)
            
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text=" TIMER ", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer_label.grid(column=1, row=0)

marks_label = Label(text="", fg=GREEN, bg=YELLOW)
marks_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

end_button = Button(text="Reset", command=reset_timer)
end_button.grid(column=2, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=IMAGE)
canvas.create_image(100, 110, image=tomato_img)
timer_change = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

window.mainloop()
