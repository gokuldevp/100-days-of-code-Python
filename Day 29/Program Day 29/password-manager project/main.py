from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# fixed constants
SAVE_PATH = "data.txt"
LOGO_PATH = "logo.png"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """function to generate password"""
    def create_password():
        """function to create a secure password"""
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_letters = [random.choice(letters) for char in range(nr_letters)]
        password_numbers = [random.choice(numbers) for num in range(nr_numbers)]
        password_symbols = [random.choice(symbols) for sym in range(nr_symbols)]
        password_list = password_symbols + password_numbers + password_letters

        random.shuffle(password_list)

        password = "".join(password_list)

        # copying password for easy use
        pyperclip.copy(password)
        return password
    password_entry.delete(0, END)
    password_entry.insert(0, create_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """function to save the password"""
    website = website_entry.get()
    email_username = email_username_entry.get()
    password_to_save = password_entry.get()

    def get_entry():
        """function to set the data in a formact"""
        return f"Website       : {website}\nEmail/Username: {email_username}\nPassword      : {password_to_save}\n\n"

    def save():
        """function to save password"""
        with open(file=SAVE_PATH, mode="a") as data:
            data.write(get_entry())

    def reset():
        """function to reset data in the canvas"""
        website_entry.delete(4, END)
        email_username_entry.delete(0, END)
        email_username_entry.insert(0, "@gmail.com")
        password_entry.delete(0, END)

    # setting warning message if data is missing
    if len(password_to_save) < 1 or len(website) < 5 or website[0:4] != "www.":
        messagebox.showwarning(title="WARNING", message="Your Data is missing! Check Your Data again?")

    # conforming if the data is ok
    else:
        add = messagebox.askokcancel(title="ADD",
                                     message=f"The data you are adding are\nWebsite: {website}\nEmail_username: {email_username}\nPassword: {password_to_save}\nAre you ok with this?")
        if add:
            save()
            reset()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Label
website_label = Label(text="website:", bg="white")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:", bg="white")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=40)
website_entry.insert(END, "www.")
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=40)
email_username_entry.insert(0, "@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21, show="*")
password_entry.grid(column=1, row=3)

# Button
password_button = Button(text="Generate Password", bg="white", command=generate_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=34, bg="white", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

# Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(50, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=2)

window.mainloop()
