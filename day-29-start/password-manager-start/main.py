from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)

    password = "".join(password_list)
    new_password(password)
def new_password(generated_password):
    password_input.delete(0, END)
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(web, info, password):
    if len(web_input.get()) > 0 and len(user_info_input.get()) > 0 and len(password_input.get()) > 0:
        is_ok = messagebox.askokcancel(title="Conformation", message=f"Do you want to save this password:\n"
                                                                     f"Email: {info}\n"
                                                                     f"Password: {password}\n"
                                                                     f"Press Yes to save\n"
                                                                     f"Press No to edit")
        if is_ok:
            with open("data.txt", 'a') as data:
                data.write(f"{web} | {info} | {password}\n")
                web_input.delete(0, END)
                password_input.delete(0, END)
    else:
        messagebox.showerror(title="Missed", message="Don't leave any field empty")

def handle_password():
    web = web_input.get()
    info = user_info_input.get()
    password = password_input.get()
    save(web, info, password)

# ---------------------------- UI SETUP ------------------------------- #

##window config
window = Tk()
window.title("Password Bank")
window.config(pady=50, padx=50)

##create a canvas to show a photo
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# button and labels config, new method on grid() using //columnspan\\

##lables
web_label = Label()
web_label.config(text="Website: ")
web_label.grid(column=0, row=1)

user_info = Label()
user_info.config(text="Email/Username:")
user_info.grid(column=0, row=2)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

##Entries
web_input = Entry(width=38, )
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()
user_info_input = Entry(width=38)
user_info_input.grid(column=1, row=2, columnspan=2)
user_info_input.insert(0, "fatkhiddinkhan@icloud.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Buttons
password_gen_but = Button(text="Generate Password", command=pass_gen)
password_gen_but.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=handle_password)
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()
