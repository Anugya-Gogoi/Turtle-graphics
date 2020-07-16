import turtle

draw = turtle.Turtle()

draw.speed(10)

turtle.bgcolor("purple")
draw.pencolor("white")
for i in range(185):
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