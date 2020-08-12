import turtle

def draw_square(some_turtle):

    for i in range (1,5):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    bonn = turtle.Turtle()
    bonn.shape("turtle")
    bonn.color("aqua")
    bonn.speed(6)
    bonn.pensize(2)
    for i in range(1,37):
        draw_square(bonn)
        bonn.right(10)
    an = turtle.Screen()
    an.shape("turtle")
    an.color("blue")
    an.speed(5)
    an.pensize(2)
    size=1
    while (True):
        an.forward(size)
        an.right(91)
        size = size + 1

    window.exitonclick()

draw_art()