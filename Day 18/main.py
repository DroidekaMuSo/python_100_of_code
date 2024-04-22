import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
t.colormode(255)
timmy.shape("turtle")
timmy.color("red")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#

# x = 0
# for _ in range(50):
#     timmy.teleport(x)
#     timmy.forward(5)
#
#     x += 10

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_in in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(shape_side_in)

# turns = [0, 1]
# size = 1
#
# for _ in range(1000):
#     timmy.color(random.choice(colours))
#     selection = random.choice(turns)
#     timmy.pensize(size)
#
#     if selection == 0:
#         timmy.left(90)
#     else:
#         timmy.right(90)
#
#     timmy.forward(20)
#
#     size += 0.1


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)

    return color


timmy.speed("fastest")

for angle in range(360):
    timmy.color(random_color())
    timmy.circle(100)

    current_heading = timmy.heading()
    timmy.setheading(current_heading+1)

# for _ in range(1000):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#






















screen = Screen()
screen.exitonclick()