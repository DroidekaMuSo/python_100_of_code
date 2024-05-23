from tkinter import *


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

def button_clicked():
    label['text'] = input.get()

#Label
label = Label(text="I'm a label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

#Button
button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="Click me!", command=button_clicked)
button_2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
