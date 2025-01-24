from tkinter import *
from tkinter import messagebox
import pandas
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pass():
    pass_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    pass_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_text = website_entry.get()
    user_text = email_user_entry.get()
    pass_text = pass_entry.get()

    print(web_text, user_text, pass_text)

    if len(web_text) == 0 or len(pass_text):
        messagebox.showerror(title="Missing Values", message="Please input details")
    else:
        proceed_save = messagebox.askokcancel(title=web_text, message=f"There are the details entered:\n"
                                                   f"Email: {user_text}\n"
                                                   f"Password: {pass_text}\n"
                                                   f"do you want to save this?")
        if proceed_save:
            with open("data.txt", "a") as data:
                text_to_save = f"{web_text} | {user_text} | {pass_text}\n"
                data.write(text_to_save)
                website_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:",)
email_user_label = Label(text="Email/Username:")
pass_label = Label(text="Password:")

website_label.grid(column=0, row=1, sticky="E")
email_user_label.grid(column=0, row=2, sticky="E")
pass_label.grid(column=0, row=3, sticky="E")

website_entry = Entry(width=35)
email_user_entry = Entry(width=35)
pass_entry = Entry(width=21)

website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
pass_entry.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", command=generate_pass)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")




window.mainloop()