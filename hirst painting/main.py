import colorgram as c
import turtle as t
import random

colors = c.extract('painting.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

t.colormode(255)
tim = t.Turtle()
x = -250
y = -250
tim.penup()

for height in range(10):
    tim.teleport(x, y)
    for width in range(10):
        color = random.choice(rgb_colors)
        tim.dot(20, color)
        tim.forward(50)
    y += 50

tim.hideturtle()



screen = t.Screen()
screen.screensize(600, 600)
screen.exitonclick()


