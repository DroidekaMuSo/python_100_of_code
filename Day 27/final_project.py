from tkinter import *

window = Tk()
window.title("Miles to KM converter")
window.minsize(width=500, height=500)

def button_clicked():
    miles = int(user_input.get())
    km = round(miles * 1.60934,2)

    label_3.config(text=km)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="0")
label_3.grid(column=1, row=1)

label_4 = Label(text="KM")
label_4.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()