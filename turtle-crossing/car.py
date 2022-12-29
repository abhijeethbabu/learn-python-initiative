from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.penup()
