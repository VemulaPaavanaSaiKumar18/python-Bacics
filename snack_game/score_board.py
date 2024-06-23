from turtle import Turtle

class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.goto(0,250)
		self.hideturtle()
		self.updateScore()
		
	
	def updateScore(self):
		self.clear()
		self.write(f"Score:{self.score}",align="center", font=("Arial", 30, "normal"))
		self.score += 1

	def game_over(self):
		self.goto(0,0)
		self.write("GAME OVER",align="center", font=("Arial", 30, "normal"))
		