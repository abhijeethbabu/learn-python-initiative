from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

is_game_running = True
while is_game_running:
    is_game_on = True
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score_board = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.new_pos()
            snake.extend()
            score_board.add_score()

        # Detect collision with wall
        if (snake.head.xcor() > 285 or snake.head.xcor() < -285 or
                snake.head.ycor() > 285 or snake.head.ycor() < -285):
            score_board.game_over()
            is_game_on = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score_board.game_over()
                is_game_on = False

    play_again = screen.textinput(title="Play Again?", prompt="Enter 'yes' to play again.")
    if play_again == 'yes':
        screen.clear()
    else:
        is_game_running = False
