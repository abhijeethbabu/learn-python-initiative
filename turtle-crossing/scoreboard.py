from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.update_level()

    def update_level(self):
        self.increase_level()
        self.clear()
        self.goto(x=-250, y=280)
        self.write(f"Level: {self.level}", True, "center", FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, "center", ("Courier", 18, "bold"))
