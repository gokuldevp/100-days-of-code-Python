from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# fixed constants
SAVE_PATH = "data.json"
LOGO_PATH = "logo.png"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """function to generate password and copy the created password"""
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
        data_dict = {
            website: {
                "Email/Username": email_username,
                "Password": password_to_save
            }
        }
        return data_dict

    def save():
        """function to save password"""
        try:
            with open(file=SAVE_PATH, mode="r") as file_data:
                # reading old data
                data = json.load(file_data)
                # updating old data
                data.update(get_entry())

        except json.decoder.JSONDecodeError:
            # adding new data to json file
            with open(file=SAVE_PATH, mode="w") as file_data:
                json.dump(get_entry(), file_data, indent=4)

        except FileNotFoundError:
            # creating a new json file
            with open(file=SAVE_PATH, mode="w") as file_data:
                json.dump(get_entry(), file_data, indent=4)
        else:
            with open(file=SAVE_PATH, mode="w") as file_data:
                # saving updated data
                json.dump(data, file_data, indent=4)

    def reset():
        """function to reset data in the canvas"""
        website_entry.delete(0, END)
        email_username_entry.delete(0, END)
        email_username_entry.insert(0, "@gmail.com")
        password_entry.delete(0, END)

    # setting warning message if data is missing
    if len(password_to_save) < 1 or len(website) < 1:
        messagebox.showwarning(title="WARNING", message="Your Data is missing! Check Your Data again?")

    # conforming if the data is ok
    else:
        add = messagebox.askokcancel(title="ADD",
                                     message=f"The data you are adding are\nWebsite: {website}\nEmail_username: {email_username}\nPassword: {password_to_save}\nAre you ok with this?")
        if add:
            save()
            reset()


# ------------------------- SEARCH PASSWORD ----------------------------#
def search_password():
    """Function to search password from the json file """
    website = website_entry.get()

    try:
        # reading the file
        with open("data.json") as file_data:
            data = json.load(file_data)

    except FileNotFoundError:
        # showing if there is no file
        messagebox.showinfo("Warning", "The file is empty!")

    except json.decoder.JSONDecodeError:
        # showing if file is empty
        messagebox.showinfo("Warning", "The file is empty!")

    else:

        try:
            # getting the site data
            website_info = data[website]

        except KeyError:
            # checking if the website name is there in password manager
            messagebox.showinfo("NO WEBSITE ADDED", f"The password of the website: '{website}' is not added in the password manager.")

        else:
            # showing the email and password
            messagebox.askokcancel(website, f"E-mail/Username: {website_info['Email/Username']}\nPassword: {website_info['Password']}")
            pyperclip.copy(website_info["Password"])


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
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_username_entry = Entry(width=40)
email_username_entry.insert(0, "@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21, show="*")
password_entry.grid(column=1, row=3)

# Button
search_button = Button(text="  Search Password  ", bg="white", command=search_password)
search_button.grid(column=2, row=1)
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
