import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pensize(3)
turtle.colormode(255)
directions = [0, 90, 180, 270, 360]

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.speed("fastest")
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + 10)
        tim.circle(100)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()

