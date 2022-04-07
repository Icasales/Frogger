from turtle import Turtle

CAVES_X_POSITIONS = [-280, -130, 20, 170, 330]
CAVES_Y_POSITION = 250


class DrawTrack(Turtle):

    def __init__(self):
        super().__init__()
        self.color("orange")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.caves_pos = []
        self.wall_pos = []
        self.caves_list = []
        self.caves()
        self.walls()
        self.draw_starting_point()

    def draw_cave(self, x, y):
        self.goto(x, y)
        self.pendown()
        self.left(90)
        self.begin_fill()
        self.circle(50, 180)
        self.end_fill()
        self.penup()
        self.home()

    def caves(self):
        # Create square turtle for measure turtle in cave
        for cave in range(len(CAVES_X_POSITIONS)):
            pocave = Turtle("square")
            pocave.penup()
            pocave.hideturtle()
            pocave.shapesize(1,4)
            pocave.goto(CAVES_X_POSITIONS[cave]-50, CAVES_Y_POSITION + 15)
            self.draw_cave(CAVES_X_POSITIONS[cave], CAVES_Y_POSITION)
            self.caves_list.append(cave)
            self.caves_pos.append(pocave)

    def walls(self):
        for cave in range(len(CAVES_X_POSITIONS)):
            wall = Turtle("square")
            wall.penup()
            wall.hideturtle()
            wall.shapesize(1,1)
            wall.goto(CAVES_X_POSITIONS[cave]+25, CAVES_Y_POSITION + 15)
            self.wall_pos.append(wall)


    def draw_starting_point(self):
        self.color("olive drab")
        self.goto(-400, -270)
        self.pensize(40)
        self.pendown()
        # self.begin_fill()
        self.goto(400, -270)
        # self.end_fill()
        self.penup()
        self.home()




