from turtle import *
bgcolor('black')

speed(0)

hideturtle()

for i in range (360):

    color('red')

    circle(i)

    color('yellow')

    circle(i*0.8)

    right(3)

    forward(3)

done()