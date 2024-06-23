from turtle import Turtle, Screen


class Paddle(Turtle):
	def __init__(self,cords):
		super().__init__()
		self.key_up = 30
		self.cord = cords
		self.hideturtle()
		self.shape("square")
		self.shapesize(stretch_wid=6,stretch_len=1,)
		self.color("green")
		self.penup()
		self.goto(self.cord)
		self.showturtle()

	def up(self):
		if self.key_up <= 230:
			self.sety(self.key_up)
			self.key_up += 30

	def down(self):
		if self.key_up >= -230:
			self.sety(self.key_up)
			self.key_up -= 30
