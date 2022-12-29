from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")
COLOR = "white"
DEFAULT_LOCATION = (0, 280)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.goto(DEFAULT_LOCATION)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(DEFAULT_LOCATION)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)
