import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

pl = Player()
car_manager = CarManager()
screen.onkey(pl.walk, "Up")
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.run_car()
    car_manager.bring_cars_back()

    # Detect collision
    for car in car_manager.cars:
        if car.distance(pl) < 20:
            score.game_over()
            game_is_on = False

    # Check if the race is over
    if pl.is_race_over():
        pl.go_back()
        car_manager.increase_car_speed()
        score.update_level()

    screen.update()

screen.exitonclick()
