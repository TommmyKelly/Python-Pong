from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_score = Scoreboard((100, 180))
l_score = Scoreboard((-100, 180))
ball = Ball()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")


def game_over():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(game_over, "p")
game_is_on = True


while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        l_score.increase_score()
        ball.reset_position()

    if ball.xcor() < -400:
        r_score.increase_score()
        ball.reset_position()

screen.exitonclick()
