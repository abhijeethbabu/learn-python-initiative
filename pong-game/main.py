import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

is_app_on = True
screen = Screen()
while is_app_on:
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    right_paddle = Paddle(pos_x=370, pos_y=0)
    left_paddle = Paddle(pos_x=-370, pos_y=0)
    ball = Ball()
    score = Scoreboard()

    screen.listen()
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")
    screen.onkey(left_paddle.go_up, "w")
    screen.onkey(left_paddle.go_down, "s")
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(ball.ball_speed)
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()

        if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
            ball.paddle_bounce()
            print(f"{ball.dx}, {ball.dy}")

        if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
            ball.paddle_bounce()
            print(f"{ball.dx}, {ball.dy}")

        if ball.xcor() > 380 and ball.distance(right_paddle) > 50:
            ball.ball_center()
            score.l_point()
            left_paddle.goto(x=-370, y=0)
            right_paddle.goto(x=370, y=0)
            time.sleep(1)

        if ball.xcor() < -380 and ball.distance(left_paddle) > 50:
            ball.ball_center()
            score.r_point()
            left_paddle.goto(x=-370, y=0)
            right_paddle.goto(x=370, y=0)
            time.sleep(1)

        if score.l_score == 12:
            is_game_on = False
            score.winner("Left")
        elif score.r_score == 12:
            is_game_on = False
            score.winner("Left")

    play_again = screen.textinput("Play again?", "Enter 'y' to play again.")
    if play_again == 'y':
        screen.clear()
    else:
        is_app_on = False

screen.exitonclick()
