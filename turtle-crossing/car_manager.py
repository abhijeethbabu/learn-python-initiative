import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LOCATION = [240, 200, 160, 120, 80, 40, 0,
            -40, -80, -120, -160, -200, -240]
INITIAL_SPEED = 10
DELTA_SPEED = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.fill_cars()
        self.speed = INITIAL_SPEED

    def run_car(self):
        for car in self.cars:
            random_choice = random.randint(1, 6)
            if random_choice == 1:
                car.backward(self.speed)

    def fill_cars(self):
        for i in range(2 * len(LOCATION)):
            y_pos = LOCATION[i % len(LOCATION)]
            car = Car()
            car.goto(x=random.choice(LOCATION), y=y_pos)
            self.cars.append(car)

    def bring_cars_back(self):
        for car in self.cars:
            if car.xcor() < -290:
                car.goto(x=300, y=car.ycor())
                car.color(random.choice(COLORS))

    def increase_car_speed(self):
        self.speed += DELTA_SPEED
