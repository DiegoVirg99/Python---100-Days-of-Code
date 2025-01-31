from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write(f"Level: {level}", align = "left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

