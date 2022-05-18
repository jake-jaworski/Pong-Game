from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    # check if ball hits upper/lower walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()

    # check if ball hits a paddle
    if (ball.xcor() >= 320 and ball.distance(paddle_right.pos()) <= 50) or (ball.xcor() <= -320 and ball.distance(paddle_left.pos()) <= 50):
        ball.x_bounce()

    # check if ball passed the paddle
    if ball.xcor() >= 390:
        score.left_scores()
        ball.reset_pos()
    elif ball.xcor() <= -390:
        score.right_scores()
        ball.reset_pos()

    # check if game is over
    if score.right_score == 2:
        score.game_over("Right Player")
        game_on = False
    elif score.left_score == 2:
        score.game_over("Left Player")
        game_on = False




screen.exitonclick()