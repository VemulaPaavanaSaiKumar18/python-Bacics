from turtle import Turtle, Screen
from snack import Snack
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My snack game")


snake = Snack()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snack()
        

screen.exitonclick()
