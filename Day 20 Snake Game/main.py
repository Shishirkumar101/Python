from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(width=600 , height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.update_score()
        food.refresh()
        snake.extend()

    for segment in snake.all_turtle[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    if snake.head.xcor()>280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor()<-280:
        game_is_on = False
        score.game_over()

screen.exitonclick()