from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong game")
screen.tracer(0)

right_player = Paddle((350, 0))
left_player = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_player.up, "Up")
screen.onkey(right_player.down, "Down")
screen.onkey(left_player.up, "w")
screen.onkey(left_player.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with the paddle
    if ball.distance(right_player) < 50 and ball.xcor() > 320 or ball.distance(left_player) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
