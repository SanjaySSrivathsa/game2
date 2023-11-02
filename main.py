from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.title("SNAKE GAME")
screen.bgcolor("black")
food=Food()
score=ScoreBoard()
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
count=0
flag=True
while flag:
    screen.update()
    time.sleep(0.05)
    snake.move()
    #collision detection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.IncreaseScore()
    snake.check_edges()

    for check in snake.segments:
        if check == snake.head:
            continue
        elif snake.head.distance(check)<10:
            flag=False
            score.gameover()
screen.exitonclick()

