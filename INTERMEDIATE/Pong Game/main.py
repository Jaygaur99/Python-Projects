from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('white')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    sleep(ball.ball_move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    screen.update()
    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()