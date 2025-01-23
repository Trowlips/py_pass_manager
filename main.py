from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=189, highlightthickness=0)
logo_img =PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_img)
canvas.grid(column=1, row=0)








window.mainloop()