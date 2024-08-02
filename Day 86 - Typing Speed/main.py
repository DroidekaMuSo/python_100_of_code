import tkinter
from tkinter import *
from PIL import Image, ImageTk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"
text_for_test = ("river this left state them over for life of far come answer because then we good head play who old "
                 "when some children from man state word great same use second only boy new same really could live "
                 "all of what could turn own day first good saw sometimes who house old most hear mean water word ask "
                 "grow great to came young hard are up people first is upon try do such make me story look large grow "
                 "was book talk world small well will sea city fire could")

text_for_val = text_for_test.split()
IMAGE_PATH = 'images/cesar-couto-TIvFLeqZ4ec-unsplash.jpg'


def start():
    window.after(60000, get_info)


def reset():
    T.delete('1.0', END)
    T.insert(tkinter.END, text_for_test)
    inputtxt.delete('1.0', END)


# widow
window = Tk()
window.title("Typing Speed Test")
window.config(pady=20, padx=20, background=BACKGROUND_COLOR, highlightthickness=0)
window.geometry("900x600")

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((900, 600)))
lbl = tkinter.Label(window, image=img)
lbl.img = img
lbl.place(relx=0.5, rely=0.5, anchor='center')

inputtxt = tkinter.Text(window,
                        height=20,
                        width=60)
T = Text(window, height=10, width=80)
T.insert(tkinter.END, text_for_test)

# Create star for next text.
b1 = Button(window, text="Start ", command=start)
title_label = Label(text="Let's Test Your Speed", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.pack()

# Create an reset button.
b2 = Button(window, text="Reset", command=reset)

T.pack()
b1.pack()
b2.pack()
inputtxt.pack()


def get_info():
    input_text = inputtxt.get("1.0", "end-1c")
    y = input_text.split()

    num = 0
    for i in y:
        if i in text_for_val:
            num += 1

    title_label.config(text=f"You reach {num} word", fg=RED)


mainloop()