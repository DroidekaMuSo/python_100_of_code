from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? \nEnter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
is_race_on = False

x = -230
y = -100

for col in range(len(colors)):
    timmy = Turtle(shape="turtle")
    timmy.speed("fastest")
    timmy.color(colors[col])
    timmy.penup()
    timmy.goto(x, y)

    all_turtles.append(timmy)

    y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won! \nThe {winning_color} turtle is the winner")
            else:
                print(f"You've lost! \nThe {winning_color} turtle is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
