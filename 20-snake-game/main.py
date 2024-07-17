"""Snake Game: Use the arrows to move the snake."""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def add_key_listeners():
    """Add key listeners"""
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.right, "d")


# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game 🐍")
# turn off turtle animation to manually update the screen (screen.update()) after moving all the segments
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

add_key_listeners()

# main game loop
game_over = False
while not game_over:
    # update the screen on each main iteration, or after moving all the segments
    screen.update()
    # set sleep time to refresh the screen
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) <= 15:
        food.go_to_random_position()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if (snake.head.xcor() < -280
            or snake.head.xcor() > 280
            or snake.head.ycor() < -280
            or snake.head.ycor() > 280):
        score.reset_score()
        snake.reset()

    # detect collision with tail
    # skip the first segment (index 0) because it's the head itself and would be always true
    for segment in snake.segments[1:]:
        # check if the head is close of the other segments
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset()


screen.exitonclick()
