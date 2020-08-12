from turtle import *
bgcolor('black')
t1=Turtle()
t1.speed(11)
x=10
for i in range(10):
    t1.color('orange')
    t1.circle(x)
    x+=10
t1.right(180)
x=10
for i in range(10):
    t1.color('pink')
    t1.circle(x)
    x+=10
t1.right(90)
x=10
for i in range(10):
    t1.color('aqua')
    t1.circle(x)
    x+=10
t1.right(-180)
x=10
for i in range(10):
    t1.circle(x)
    x+=10

done()