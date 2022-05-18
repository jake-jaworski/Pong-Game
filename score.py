from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("grey")
        self.left_score = 0
        self.right_score = 0
        self.score_update()

    def right_scores(self):
        self.right_score += 1
        self.score_update()

    def left_scores(self):
        self.left_score += 1
        self.score_update()

    def increment_score(self):
        self.clear()
        self.points += 1
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))

    def game_over(self, winner):
        self.goto(0, 0)
        self.write(f"Game over! {winner} wins!", align="center", font=('Courier', 24, 'normal'))

