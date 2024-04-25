from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)

    def up(self):
        if self.ycor() < 250:
           self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 20)

