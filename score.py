

from turtle import Turtle


class Score(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.score = 0
		self.hideturtle()
		self.speed(0)
		self.penup()
		self.goto(0, 275)
		self.write("Score = 0", align="center", font=('Arial', 15, 'normal'))



	def eatfood(self):
		self.clear()
		self.score += 1
		self.write(f"Score = {self.score}", align="center", font=('Arial', 15, 'normal'))


	def gameover(self):
		self.goto(0,0)
		self.color("green")
		self.write("GAME OVER", align="center", font=('Arial', 25, 'normal'))