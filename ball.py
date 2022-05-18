from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_paces = 10
        self.y_paces = 10

    def move_ball(self):
        new_ycor = self.ycor() + self.y_paces
        new_xcor = self.xcor() + self.x_paces
        self.goto(new_xcor, new_ycor)

    def y_bounce(self):
        self.y_paces *= (-1)

    def x_bounce(self):
        self.x_paces *= (-1)

    def reset_pos(self):
        self.goto(0, 0)
        self.x_bounce()

