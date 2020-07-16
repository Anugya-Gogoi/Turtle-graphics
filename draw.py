import turtle
from random import randint
draw = turtle.Turtle()

draw.speed(10)

turtle.bgcolor("black")


for i in range(185):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    turtle.colormode(255)
    draw.pencolor(r, g, b)
    draw.forward(90)
    draw.right(30)
    draw.forward(20)
    draw.left(60)
    draw.forward(50)
    draw.right(30)

    draw.penup()
    draw.setposition(0, 0)
    draw.pendown()

    draw.right(2)



turtle.done()
