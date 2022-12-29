from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def walk(self):
        self.forward(MOVE_DISTANCE)

    def is_race_over(self):
        return self.ycor() > 280

    def go_back(self):
        self.goto(STARTING_POSITION)
