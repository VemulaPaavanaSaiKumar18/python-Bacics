from turtle import Turtle, Screen
from snack import Snack
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=900, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My snack game")

snake = Snack()
food = Food()
score_board = ScoreBoard()

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
		
    if snake.snack_segments[0].distance(food) < 15:
      food.refresh()
      score_board.updateScore()
      snake.extend_segment()
      
    if snake.snack_segments[0].xcor() > 435 or snake.snack_segments[0].ycor() > 295 or snake.snack_segments[0].xcor() < -435 or snake.snack_segments[0].ycor() < -295:
      game_on = False
      score_board.game_over()
    for segments in snake.snack_segments[1:]:
        if snake.snack_segments[0].distance(segments) < 10:
        # segments == snake.snack_segments[0]
           game_on = False
           score_board.game_over()
            
        

screen.exitonclick()
