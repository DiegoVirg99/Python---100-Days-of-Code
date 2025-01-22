import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
car_list = []

car_generation=1
level=1
scoreboard = Scoreboard(level)
i=1

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_generation += 1
    if car_generation % 6 == 0:
        car = CarManager()
        j = 1
        while j < level:
            car.increase_speed()
            j += 1
        car_list.append(car)
    for item in car_list:
        item.move()
        if 20 > player.distance(item):
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= 280:
        player.start()
        level +=1
        scoreboard.clear()
        scoreboard = Scoreboard(level)
    if i<level:
        for auto in car_list:
            auto.increase_speed()
            i += 1


screen.exitonclick()
