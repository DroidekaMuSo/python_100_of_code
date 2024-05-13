import tkinter
import turtle

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label
label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold"))
label.pack(side='left')

tim = turtle.Turtle()
tim.write()

window.mainloop()
