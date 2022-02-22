from turtle import Turtle,Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle=Paddle((360,0))
l_paddle=Paddle((-360,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.pong_up,"Up")
screen.onkey(l_paddle.pong_up,"w")
screen.onkey(r_paddle.pong_down,"Down")
screen.onkey(l_paddle.pong_down,"s")



game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Ball bounces off top and bottom walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #Ball touches the paddle and bounces
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()


    #Ball Misses the right Paddle
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()


    #Ball Misses the left paddle
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()















screen.exitonclick()