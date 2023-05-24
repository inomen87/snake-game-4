from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import  Score


screen = Screen()


screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake New")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
	screen.update()
	time.sleep(0.3)
	snake.move()


	if snake.segments[0].distance(food) < 19:
		food.refresh()
		score.eatfood()
		snake.extend()


	if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() > 295 or snake.segments[0].ycor() < -295:
		game_is_on = False
		score.gameover()


	for item in snake.segments[1:]:
		if snake.segments[0].distance(item) < 10:
			game_is_on = False
			score.gameover()













screen.exitonclick()