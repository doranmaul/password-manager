from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# TODO: Build a function that saves data from entry fields when clicking "add" button to a new file called data.txt
# TODO: Incorporate erase field functionality into the function


def save():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        website_is_empty = messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n {email} \n {password} \n Is it okay to save?")
        if is_ok:
            with open("passwords.text", "a") as data:
                data.write(f"{website} | {email} | {password} \n")
                password_entry.delete(0, END)
                website_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

# TODO: 3 labels, 3 entries, two buttons

# 3 columns, 5 rows
# Website entry 35 width, Password entry 21 width, add button 36 width

# Label 1

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Label 2

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

# Label 3

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry 1

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="nsew")
website_entry.focus()

# Entry 2

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="nsew")
email_user_entry.insert(0, "email_address@gmail.com")

# Entry 3

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="nsew")

# Button 1

generate_button = Button(text="Generate Password", command=pass_generator)
generate_button.grid(column=2, row=3,)

# Button 2

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="nsew")


password_logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200, highlightthickness=0)
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)


window.mainloop()
