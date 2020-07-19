import turtle
screen=turtle.Screen()
jamie=turtle.Turtle()
screen.setup(620,620)
screen.bgcolor('black')
clr=['red','green','blue','yellow','purple']
jamie.pensize(2)
jamie.shape('turtle')
jamie.penup()
jamie.pencolor('aqua')
m=0
for i in range(12):
      m=m+1
      jamie.penup()
      jamie.setheading(-30*i+60)
      jamie.forward(150)
      jamie.pendown()
      jamie.forward(25)
      jamie.penup()
      jamie.forward(20)
      jamie.write(str(m),align="center",font=("Arial Black", 12, "normal"))
      if m==12:
        m=0
      jamie.home()
jamie.home()
jamie.setpos(0,-250)
jamie.pendown()
jamie.pensize(6)
jamie.pencolor('white')
jamie.circle(250)
jamie.penup()
jamie.setpos(150,-270)
jamie.pendown()
jamie.pencolor('olive')
jamie.write('Anugya',font=("Vivaldi", 14, "bold"))
jamie.done()