from turtle import Turtle
import random

class Snack:
	def __init__(self):
		self.snack_position = [(0, 0), (-20, 0), (-40, 0)]
		self.snack_segments = []
		self.form_snack()
	def form_snack(self):
		for segment in self.snack_position:
			self.add_segment(segment)

	def add_segment(self,segment):
		new_segment = Turtle(shape="square")
		new_segment.penup()
		new_segment.color("green")
		new_segment.goto(segment)
		self.snack_segments.append(new_segment)
	
	def extend_segment(self):
		self.add_segment(self.snack_segments[-1].position())

	def move_snack(self):
		for seg_num in range(len(self.snack_segments) - 1, 0, -1):
			new_x = self.snack_segments[seg_num - 1].xcor()
			new_y = self.snack_segments[seg_num - 1].ycor()
			self.snack_segments[seg_num].goto(new_x, new_y)
		self.snack_segments[0].forward(20)

	def up(self):
		if self.snack_segments[0].heading() != 270:
			self.snack_segments[0].setheading(90)

	def down(self):
		if self.snack_segments[0].heading() != 90:
			self.snack_segments[0].setheading(270)

	def left(self):
		if self.snack_segments[0].heading() != 0:
			self.snack_segments[0].setheading(180)

	def right(self):
		if self.snack_segments[0].heading() != 180:
			self.snack_segments[0].setheading(0)