from turtle import Turtle
import random
DIRECTION = [0, 90, 180, 270]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("violet")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(x=random_x, y=random_y)

    def new_pos(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        while random_x == self.xcor():
            random_x = random.randint(-275, 275)
        self.setheading(random.choice(DIRECTION))
        self.goto(x=random_x, y=random_y)
