import turtle
turtle.bgcolor('black')
def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(40)
        tree(branchLen-17,t)
        t.left(80)
        tree(branchLen-17,t)
        t.right(40)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(110)
    t.down()
    t.pensize('4')
    t.color("green")
    tree(85,t)
    myWin.exitonclick()

main()