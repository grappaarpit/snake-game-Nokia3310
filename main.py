from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
score_now = 0
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move(15)
    if snake.segments[0].distance(food) < 15 :
        food.refresh()
        snake.extend()
        score_now+=1
        score.Score_update(score_now)

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 285 or snake.segments[0].ycor() < -285:
        game_is_on = False

    for segments in snake.segments[1:]:
        if snake.segments[0].distance(segments)<10:
            game_is_on = False

score.game_over()



screen.exitonclick()