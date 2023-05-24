

from turtle import Turtle

class Snake:

	def __init__(self):
		self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
		self.segments = []
		self.create_snake()




	def create_snake(self):
		for item in self.starting_positions:
			self.addsegment(item)

	def move(self):
		for num in range(len(self.segments) - 1, 0, -1):
			newx = self.segments[num - 1].xcor()
			newy = self.segments[num - 1].ycor()
			self.segments[num].goto(newx, newy)

		self.segments[0].forward(20)


	def addsegment(self, item):
		new_segment = Turtle("square")
		new_segment.penup()
		new_segment.color("white")
		new_segment.goto(item)
		self.segments.append(new_segment)

	def extend(self):
		self.addsegment(self.segments[-1].position())



	def up(self):
		if self.segments[0].heading() != 270:
			self.segments[0].setheading(90)

	def down(self):
		if self.segments[0].heading() != 90:
			self.segments[0].setheading(270)

	def left(self):
		if self.segments[0].heading() != 0:
			self.segments[0].setheading(180)

	def right(self):
		if self.segments[0].heading() != 180:
			self.segments[0].setheading(0)