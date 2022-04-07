from turtle import Turtle
UP = 90


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 1
        self.lives_remaining = 3
        self.lives_frogs = []
        #self.lives_keep_track()
        self.live_sign()

    def lives_keep_track(self):
        # Shows lives remaining in turtle form
        live_position = -350
        x_list = []

        for x in range(self.lives_remaining):
            live_position += 15
            x_list.append(live_position)

        for live in range(self.lives_remaining):
            frog_lives = Turtle("turtle")
            frog_lives.penup()
            frog_lives.color("purple")
            frog_lives.shapesize(0.8, 0.8)
            frog_lives.setheading(UP)
            frog_lives.goto(x_list[live], -280)
            self.lives_frogs.append(frog_lives)

    def reset_turtles_lives(self):
        for live in self.lives_frogs:
            live.reset()
            live.hideturtle()

    def live_sign(self):
        self.goto(-390, -280)
        self.write("Lives: ", align="left", font= ("SimSun", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!!", align="center", font=("SimSun", 35, "normal"))

    def update_level(self):
        self.goto(300, -280)
        self.write(f"Level: {self.level}", align="left", font= ("SimSun", 16, "normal"))

    def keep_level(self):
        self.clear()
        self.level += 1
        self.update_level()
        self.live_sign()

    def update_score(self):
        self.goto(150, -280)
        self.write(f"Score: {self.score}", align="left", font= ("SimSun", 16, "normal"))

    def keep_score(self):
        self.clear()
        self.score += self.level
        self.update_score()
        self.live_sign()






    # def splash(self):
    #     splash = Turtle()
    #     splash.goto(0, 0)
    #     splash.penup()
    #     splash.hideturtle()
    #     splash.color("red")
    #     splash.write("SPLASHHHH!!!", align="center", font=("SimSun", 35, "normal"))
    #     splash.reset()


