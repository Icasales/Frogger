from turtle import Turtle
import random
Y_POSITIONS = [-220, -170, -130, -80, -30, 30, 80, 130, 170, 220]
X_POSITIONS_R = [-250, -40, 120, 390]
X_POSITIONS_L = [-290, -80, 80, 390]
LEFT = 180
RIGHT = 0
COLORS = ["purple", "blue", "green", "yellow", "orange", "red", "black", "DarkBlue", "brown", "cyan"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("dark gray")
        self.blue_cars = []
        self.lines_right()
        self.red_cars = []
        self.lines_left()
        self.cars_speed = 3

    def lines_right(self):
        for car in range(len(X_POSITIONS_R)):
            pos_y = Y_POSITIONS[::2]

            for cars in range(len(Y_POSITIONS[::2])):
                pos = X_POSITIONS_R[car]
                new_car = Turtle(shape="square")
                new_car.color(random.choice(COLORS))
                new_car.penup()
                new_car.shapesize(1.5, 3, 1)
                new_car.goto(pos, pos_y[cars])
                new_car.setheading(LEFT)
                self.blue_cars.append(new_car)

    def lines_left(self):
        for car in range(len(X_POSITIONS_L)):
            pos_y = Y_POSITIONS[1::2]

            for cars in range(len(Y_POSITIONS[::2])):
                pos = X_POSITIONS_L[car]
                new_car = Turtle(shape="square")
                new_car.color(random.choice(COLORS))
                new_car.penup()
                new_car.shapesize(1.5, 3, 1)
                new_car.goto(pos, pos_y[cars])
                new_car.setheading(RIGHT)
                self.red_cars.append(new_car)

    def move(self):
        for car in self.blue_cars:
            car.forward(self.cars_speed)
            if car.xcor() < -400:
                car.setx(400)
        for car in self.red_cars:
            car.forward(self.cars_speed)
            if car.xcor() > 400:
                car.setx(-400)

    def remove_cars(self):
        # if next level, more speed an less cars, hide static car in dark grey
        remove_red_car = random.choice(self.red_cars)
        remove_red_car.color("dark grey")
        remove_red_car.goto(-401, -401)

        remove_blue_car = random.choice(self.blue_cars)
        remove_blue_car.color("dark grey")
        remove_blue_car.goto(-401, -401)

        self.red_cars.remove(remove_red_car)
        self.blue_cars.remove(remove_blue_car)
        #self.clear()

