from turtle import * # imports the module turtle, #* stands for all, which makes things easier
from random import randint

speed(0) # sets the speed of drawing to 0, which is the fastest
bgcolor('black') # sets the color of the background/canvas to black

x = 0 # creates a variable x with value 0
up() # lifts up the pen, so no lines are drawn


rt(45)
fd(90)
rt(135)

down() # sets down the pen, so that turtle can draw
while x < 120: # while the value of x is lesser than 120, #continuously do this
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    colormode(255)
    pencolor(r, g, b)
    fd(150)
    rt(61)
    fd(150)
    rt(61)
    fd(150)
    rt(61)
    fd(150)
    rt(61)
    fd(150)
    rt(61)
    fd(150)
    rt(61)

    rt(11.1111)
    x = x+1 # adds 1 to the value of x,
            # so that it is closer to 120 after every loop

exitonclick() # When you click, turtle exits.