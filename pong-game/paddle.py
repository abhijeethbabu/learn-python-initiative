from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=pos_x, y=pos_y)

    def go_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 40)

    def go_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 40)
