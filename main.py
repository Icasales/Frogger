from turtle import Screen, Turtle
from track import DrawTrack
from frogs import Frog
from cars import Car
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("dark gray")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("My Frogger")

draw = DrawTrack()
frog = Frog()
cars = Car()
score = Score()

screen.listen()
screen.onkey(frog.go_up, "Up")
screen.onkey(frog.go_down, "Down")
screen.onkey(frog.go_left, "Left")
screen.onkey(frog.go_right, "Right")

print(draw.caves_list)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    cars.move()
    score.lives_keep_track()
    score.update_level()
    score.update_score()

    # if turtle goes to cave, position turtle in cave
    for cave in draw.caves_pos:
        if frog.distance(cave) < 40:
            frog.frog_in_cave(cave.pos())
            score.keep_score()
            frog.reset_position()

    # if turtle already in cave, lose a life
    for home in frog.frog_home_list:
        if frog.frog_home_list.count(home) > 1:
            print("splash")
            score.lives_remaining -= 1
            score.reset_turtles_lives()
            frog.frog_home_list.pop()

    # if turtle goes to end point and hit wall, lose a life
    for wall in draw.wall_pos:
        if frog.distance(wall) < 30:
            score.lives_remaining -= 1
            score.reset_turtles_lives()
            frog.reset_position()
            print(score.lives_remaining)

    # Detect collision with cars from right
    for car in cars.blue_cars:
        if frog.distance(car) < 40:
            score.lives_remaining -= 1
            print(score.lives_remaining)
            score.reset_turtles_lives()
            frog.reset_position()

    # Detect collision with cars from left
    for car in cars.red_cars:
        if frog.distance(car) < 40:
            score.lives_remaining -= 1
            print(score.lives_remaining)
            score.reset_turtles_lives()
            frog.reset_position()

    # all frog in caves, next level
    if len(frog.frog_home_list) == len(draw.caves_pos):
        frog.reset_frogs_in_cave()
        cars.cars_speed += 1
        cars.remove_cars()
        cars.move()
        score.keep_level()

    if score.lives_remaining == -1:
        score.game_over()
        game_on = False

screen.exitonclick()
