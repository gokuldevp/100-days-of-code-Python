# *************************************************** Import ***********************************************************
import tkinter as tk
from datetime import datetime


# *************************************************** Variables ********************************************************
click_time = 0
current_time = 0


# *************************************************** Functions ********************************************************
def update(event):
    """Get the value of time when we release the key."""
    global click_time
    click_time = int(str(datetime.now().time()).split(":")[1])*60 + float(str(datetime.now().time()).split(":")[-1])
    window.after(5000, updated_time)


def updated_time():
    """Get the value of time after 5 sec."""
    global current_time
    current_time = int(str(datetime.now().time()).split(":")[1])*60 + float(str(datetime.now().time()).split(":")[-1])


def check():
    """Check the Difference between time when we release the key and value of time after 5 sec if the difference is more
    than 5 sec then clear the text in the Text box"""
    if current_time - click_time > 5:
        text.delete("1.0", "end")
    window.after(50, check)


# *************************************************** Main *************************************************************
# Creating and config Window
window = tk.Tk()
window.title("Disappearing Text Writing App")
window.minsize(600, 600)
window.maxsize(600, 600)

# Creating and config Label
label_1 = tk.Label(text="Write Something", font=("Times New Roman", 18))
label_2 = tk.Label(text="What you write will Disappear after 5 second", font=("Times New Roman", 14))
label_1.place(relx=.36, rely=0)
label_2.place(relx=.23, rely=.05)

# Creating and config Text
text = tk.Text(width=74, height=33)
text.place(relx=.004, rely=.1)

# setting bind so that when key is released after 5 sec the text is removed from text widget
window.bind("<KeyRelease>", update)
window.after(50, check)

window.mainloop()

# **********************************************************************************************************************
