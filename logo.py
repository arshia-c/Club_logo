import turtle
a=turtle.Turtle()
bg=turtle.Screen()
bg.bgcolor("#990000")
a.color("white","white")
a.pensize(7)
def go(x,y):
    a.penup()
    a.goto(x,y)
    a.pendown()
   
go(-30,-100)
a.forward(55)
a.circle(10,90)
a.forward(50)
a.circle(-20,60)
a.circle(90,300)
a.circle(-20,60)
a.forward(50)
a.circle(10,90)

go(-30,-100)
a.seth(-70)
a.circle(32,140)

a.seth(0)
go(-34,-85)
a.forward(65)

a.seth(0)
go(-34,-71)
a.forward(65)

a.seth(90)
go(-12,-71)
a.forward(55)

a.seth(90)
go(9,-71)
a.forward(55)

a.seth(0)
go(-18,-25)
a.forward(33)

#inner circle
go(0,4) 
a.circle(60)

#code line
go(-8,35)
a.seth(75)
a.forward(70)

#code
go(-18,50)
a.left(60)
a.forward(30)
a.right(90)
a.forward(30)

go(10,46)
a.right(15)
a.forward(30)
a.left(95)
a.forward(30)

#line
go(-130,50)
a.right(140)
a.forward(20)

go(-95,100)
a.right(15)
a.backward(20)

go(-65,160)
a.right(25)
a.forward(20)

go(-5,180)
a.right(25)
a.forward(20)

go(65,170)
a.right(35)
a.forward(20)

go(95,100)
a.right(25)
a.backward(20)

go(135,50)
a.right(45)
a.forward(20)

go(4,-200)
a.pencolor("white")
style=("times new roman",50,"bold")
a.write("CODER'S CLUB",font=style,align="center")

go(0,-230)
a.pencolor("white")
style=("lucida handwriting",15,"bold")
a.write("Code.Commit.Collaborate",font=style,align="center")


turtle.done()





