import tkinter

# creating a window in tkinter and setting it up
window1 = tkinter.Tk()
window1.title("My first GUI")
window1.minsize(width=1000, height=500)

# we need to use pack(),grid() or place() function to see the object in the window
# in pack() we can place the object on top,left,right and down
# in place() we can place the object according to x and y axis
# in grid() we can place the object according to rows and column on the window, here window is considered as a grid


# creating a label in tkinter and setting it up,
my_label = tkinter.Label(text="I Am Gokul", font=("Times New Roman", 35))
my_label.pack(side="top")
# changing argument(eg:text) in label
my_label["text"] = "I am Gokul Dev"
# or
my_label.config(text="Gokul Dev.P")


# creating a button in tkinter and setting it up,

def button_click():
    button_label["text"] = "Button clicked"


button_label = tkinter.Label(text="Button is not clicked", font=("Times New Roman", 50))
button_label.pack()
button = tkinter.Button(text="click me", command=button_click)
button.pack()


# creating a Entry in tkinter and setting it up,

def click_button():
    data = entry.get()
    entry_label.config(text=data)
    entry_label.pack()


entry = tkinter.Entry()
entry.pack()
entry_label = tkinter.Label()
button_2 = tkinter.Button(text="data enter", command=click_button)
button_2.pack()
window1.mainloop()
# ******************************************************************************************************************

# using grid for place object
# use padx and pady to make space between object
window2 = tkinter.Tk()
window2.title("My second GUI")
window2.config(padx=25, pady=25)

label = tkinter.Label(text="new label")
label.grid(column=0, row=0)
label.config(padx=25, pady=25)
button1 = tkinter.Button(text="button 1")
button1.grid(column=1, row=1)
button2 = tkinter.Button(text="button 1")
button2.grid(column=2, row=0)
new_entry = tkinter.Entry(text="enter the text")
new_entry.grid(column=3, row=2)
window2.mainloop()
