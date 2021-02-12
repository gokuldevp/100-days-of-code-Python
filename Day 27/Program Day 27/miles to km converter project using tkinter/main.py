from tkinter import *


# function to convert miles to km
def calculate():
    miles = int(miles_value.get())
    km = round(miles * 1.609344, 2)
    km_value["text"] = km


# create and setup window
window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)

# create button to run calculate function
button = Button(text="CONVERT", command=calculate)
button.grid(column=2, row=3)

# create constant labels that need to be shown on the window
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=2)
km_label = Label(text="Km")
km_label.grid(column=3, row=2)
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

# create label for km value
km_value = Label(text=0.0)
km_value.grid(column=2, row=2)

# create entry for miles
miles_value = Entry(text="0", width=10)
miles_value.grid(column=2, row=1)

window.mainloop()
