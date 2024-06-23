from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time


screen = Screen()

screen.bgcolor("black")
screen.title("PONG")
screen.setup(900, 600)
screen.tracer(0)

r_paddle = Paddle((410,0))
l_paddle = Paddle((-410,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s	")

game_on = True

while game_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
		ball.bounce_x()

	if ball.xcor() > 450:
		ball.reset_position()

	if ball.xcor() < -450:
		ball.reset_position()

screen.exitonclick()