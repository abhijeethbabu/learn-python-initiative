from turtle import Turtle

DEFAULT_SPEED = 0.001
DEFAULT_LOCATION = (0, 0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.dx = 10
        self.dy = 10
        self.ball_speed = DEFAULT_SPEED

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.dy *= -1

    def paddle_bounce(self):
        self.dx *= -1
        self.ball_speed *= 0.9

    def ball_center(self):
        self.goto(DEFAULT_LOCATION)
        self.ball_speed = DEFAULT_SPEED
        self.dx *= -1
