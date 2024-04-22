import colorgram
import random
from turtle import Turtle, Screen
import turtle as t

t.colormode(255)

timmy = Turtle()
color_list = [(229, 222, 210), (223, 159, 80), (39, 107, 149), (118, 164, 192), (150, 63, 88), (207, 134, 157), (180, 160, 35), (28, 133, 96), (213, 86, 59), (120, 181, 152), (164, 80, 52), (200, 84, 111), (208, 225, 215), (143, 31, 40), (54, 167, 135), (232, 198, 110), (201, 219, 227), (229, 206, 214), (6, 109, 90), (41, 160, 185), (117, 114, 163), (238, 159, 174), (30, 62, 112), (153, 211, 199), (235, 169, 158), (26, 64, 57), (125, 38, 35), (28, 58, 84), (150, 208, 217), (69, 39, 50)]
timmy.speed("fastest")
timmy.hideturtle()

for y in range(10):
    timmy.sety(y)

    for x in range(10):
        timmy.setx(x)
        timmy.dot(1, random.choice(color_list))

screen = Screen()
screen.exitonclick()
