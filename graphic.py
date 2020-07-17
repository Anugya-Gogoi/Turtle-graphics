from turtle import *

from random import randint

speed(0)

bgcolor('black')

x = 1

while x < 300:

    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colormode(255)
    pencolor(r,g,b)

    forward(20 + x)
    right(35)
    left(95)
    right(25)
    backward(17)


    x = x+1

turtle.exitonclick()