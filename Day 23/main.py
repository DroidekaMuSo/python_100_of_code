from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(600, 600)
screen.title("Turtle-Crossing game")
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()





screen.exitonclick()

