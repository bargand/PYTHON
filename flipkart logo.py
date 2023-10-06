import turtle
t=turtle.Turtle()

t.speed(3)

t.hideturtle()

t.pensize(3)

t.penup()

t.goto(-100,100)

t.pendown()

t.color("yellow")

t.begin_fill()

t.rt(90)

t.fd(300)

t.lt(2)

t.circle(30,90)

t.rt(2)

t.fd(300)

t.circle(30,90)

t.fd(300)

t.lt(90)

t.fd(360)

t.end_fill()

t.color("gold")

t.begin_fill()

t.rt(135)

t.fd(70)

t.lt(90)

t.fd(30)

t.rt(115)

t.fd(40)

t.rt(20)

t.fd(250)

t.rt(20)

t.fd(40)

t.rt(115)

t.fd(30)

t.lt(75)

t.fd(60)

t.rt(120)

t.fd(364)

t.end_fill()

t.penup()

t.goto(20,160)

t.pendown()

t.color("black")

t.begin_fill()

t.circle(5)

t.end_fill()

t.penup()

t.goto(150,160)

t.pendown()

t.color("black")

t.begin_fill()

t.circle(5)

t.end_fill()

t.penup()

t.goto(20,75)

t.pendown()

t.pencolor("white")

t.pensize(5)

t.lt(90)

t.circle(70,180)

t.penup()

t.goto(90,-226)

t.pendown()

t.color("royal blue")

t.begin_fill()

t.rt(10)

t.fd(65)

t.lt(100)

t.fd(150)

t.rt(90)

t.fd(3)

t.rt(90)

t.fd(100)

t.lt(90)

t.fd(10)

t.lt(90)

t.fd(50)

t.rt(90)

t.fd(3)

t.rt(90)

t.fd(50)

t.lt(90)

t.fd(10)

t.lt(90)

t.fd(100)

t.rt(90)

t.fd(3)

t.rt(90)

t.fd(150)

t.lt(90)

t.circle(-120,90)

t.rt(2)

t.circle(-5,90)

t.fd(40)

t.rt(2)

t.circle(-5,90)

t.circle(70,90)

t.lt(90)

t.fd(30)

t.circle(-20,180)

t.fd(30)

t.lt(85)

t.fd(65)

t.rt(81)

t.fd(50)

t.end_fill()

t.penup()

t.goto(-100,-350)

t.pendown()

t.write("Flipkart",font=("vardana",20,"normal"))

t.penup()

t.goto(-500,-1000)

t.pendown()

t.write("developed by\n @debu vai",font=("vardana",10,"bold","italic"))

turtle.done()