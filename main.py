from tkinter import *
from tkinter import messagebox
import math
import random
import string


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    s11 =  []
    s1 = list(string.ascii_lowercase)
    for i in range(random.randint(4,6)):
        s11.append(random.choice(s1))

    s2 = list(string.ascii_uppercase)
    for i in range(random.randint(4, 6)):
        s11.append(random.choice(s2))

    s3 = list(string.digits)
    for i in range(random.randint(4, 6)):
        s11.append(random.choice(s3))
    s4 = list(string.punctuation)
    for i in range(random.randint(4, 6)):
        s11.append(random.choice(s4))

    password = "".join(s11)
    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    website_entry.focus()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error Message", message="Not enough lenght")

    else:
        is_ok = messagebox.askokcancel(title="Confirm the info", message=f"Website: {website}\n "
                                                                         f"username: {email}\npassword: {password}\n is it okay to save?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"website: {website}, email: {email}, password: {password} \n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")

# Canvas
canvas = Canvas(width=200, height=190)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 85, image=logo)
canvas.grid(column=2, row=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)
password_label = Label(text="Password")
password_label.grid(row=4, column=1)

# entry

website_entry = Entry(width=38)
website_entry.grid(row=2, column=2, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=3, column=2, columnspan=2)
password_entry = Entry()
password_entry.grid(row=4, column=2)

# Buttons
generate_password_button = Button(text="Generate Password", bg="white", command=password_generator)
generate_password_button.grid(row=4, column=3)
add_button = Button(text="Add", width=32, bg="white", command=save)
add_button.grid(row=5, columnspan=2, column=2)

window.mainloop()
