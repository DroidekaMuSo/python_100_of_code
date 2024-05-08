import pandas, turtle

data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
checking_guess = data[data['state'] == answer_state]

if len(checking_guess) > 0:
    turtle.write(checking_guess["state"])

turtle.mainloop()


