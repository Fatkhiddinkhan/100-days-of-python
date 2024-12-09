import random
from tkinter import *

import pandas
from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
#dictionary data config
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
except EmptyDataError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")




def next_word():
    ## random word pick up from data list
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    ##print new word
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=card_front)
    flip_timer = window.after(3000, func=card_flip)

def card_flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])
    canvas.itemconfig(card_img, image=card_back)

def known_words():
    to_learn.remove(current_card)
    print(len(to_learn))
    dt = pandas.DataFrame(to_learn)
    dt.to_csv("data/words_to_learn.csv", index=False)
    next_word()

#window config
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
window.title("Flashy")
flip_timer = window.after(3000, func=card_flip)


#images location
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
img_right = PhotoImage(file="./images/right.png")
img_wrong = PhotoImage(file="./images/wrong.png")

#canvas image text config
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", fill="black", font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="", fill="black", font=('Ariel', 60, 'bold'))

#button config
right_button = Button(image=img_right, highlightthickness=0, bd=0, relief=FLAT, command=known_words)
right_button.grid(row=1, column=1)
wrong_button = Button(image=img_wrong, highlightthickness=0, bd=0, relief=FLAT, command=next_word)
wrong_button.grid(row=1, column=0)

##start with new word
next_word()









window.mainloop()