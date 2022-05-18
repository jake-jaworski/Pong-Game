from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def move_up(self):
        new_cor = self.ycor() + 20
        self.goto(self.xcor(), new_cor)

    def move_down(self):
        new_cor = self.ycor() - 20
        self.goto(self.xcor(), new_cor)
