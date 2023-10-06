##multipol dot method
import turtle
t=turtle.Turtle()
t.hideturtle()
t.penup()
t.pencolor("red")
list=["green" , "red" , "blue" , "black"]
for i in range(4):
    t.dot(50)
    t.fd(100)
t.home()
for i in range(4):
    t.dot(50)
    t.backward(100)

turtle.done()