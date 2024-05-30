from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TIME = 3000
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/es_en.csv").to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data)
    canvas.itemconfig(card_title, text="English", fill="Black")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="Black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(TIME, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)

    canvas.itemconfig(card_title, text="Español", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['Español']}", fill="white")


def known_card():
    data.remove(current_card)

    updated_data = pandas.DataFrame(data)
    updated_data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(TIME, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=known_card)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()
