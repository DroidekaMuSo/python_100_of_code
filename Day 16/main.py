# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(300)
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Pokemon",['Electric', 'Water', 'Fire'])

table.align = 'l'

print(table)
