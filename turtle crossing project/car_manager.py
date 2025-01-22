from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250,250))
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

