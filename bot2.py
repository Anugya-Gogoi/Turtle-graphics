import turtle

prim = turtle.Turtle()

turtle.bgcolor("black")
prim.pencolor("blue")

for i in range(50):
    prim.forward(80)
    prim.left(123)

prim.pencolor("red")
for i in range(50):
    prim.forward(120)
    prim.left(123)

prim.pencolor("purple")
for i in range(50):
    prim.forward(150)
    prim.left(123)
turtle.exitonclick()