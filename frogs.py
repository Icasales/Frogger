from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 50
START_POINT = (0, -280)


class Frog(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(START_POINT)
        self.setheading(UP)
        self.shapesize(1.3, 1.3, 1)
        self.frog_home_list = []
        self.frogs_in_cave = []

    def move(self):
        self.forward(DISTANCE)

    def go_up(self):
        self.setheading(UP)
        self.forward(DISTANCE)

    def go_down(self):
        self.setheading(DOWN)
        self.forward(DISTANCE)

    def go_left(self):
        self.setheading(LEFT)
        self.forward(DISTANCE)

    def go_right(self):
        self.setheading(RIGHT)
        self.forward(DISTANCE)

    def reset_position(self):
        self.goto(START_POINT)

    def frog_in_cave(self, position):
        frog_home = Turtle("turtle")
        frog_home.color("green")
        frog_home.penup()
        frog_home.shapesize(1.5, 1.5)
        frog_home.setheading(DOWN)
        frog_home.goto(position)
        self.frog_home_list.append(position)
        self.frogs_in_cave.append(frog_home)

        print(self.frog_home_list)

    def reset_frogs_in_cave(self):
        #reset turtles in cave for next level
        self.frog_home_list = []
        for frog in self.frogs_in_cave:
            frog.reset()
            frog.hideturtle()
