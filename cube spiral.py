# import turtle

# t=turtle.Turtle()

# t.pensize(4)

# for i in range (200):

#     t.fd(200)

#     t.lt(90)

#     t.fd(200)

#     t.lt(90)

#     t.fd(200)

#     t.lt(90)

#     t.fd(200)

#     t.lt(90)

#     t.rt(15)

# t.fd(200)

# t.lt(90)

# t.fd(200)

# t.lt(90)

# t.fd(200)

# t.lt(90)

# t.fd(200)

# t.lt(90)

# t.rt(15)




# R G B COLOR GRADIANT  with while loop

import turtle
from random import randint
t = turtle.Turtle()
t.pensize(4)
t.speed(0)
x=1
while x<400:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.colormode(255)
    t.pencolor(r, g, b)

    t.fd(200)

    t.lt(90)

    t.fd(200)

    t.lt(90)

    t.fd(200)

    t.lt(90)

    t.fd(200)

    t.lt(90)

    t.rt(15)
x=x+1
t.done()





# R G B COLOR GRADIANT  with for loop

# import turtle
# from random import randint
# t = turtle.Turtle()
# t.pensize(4)
# t.speed(0)

# for i in range (400):
#     r = randint(255,165,0)
#     g = randint(132,112,255)
#     b = randint(0,128,0)
#     #turtle.colormode(255)
#     t.pencolor(r, g, b)

#     t.fd(200)

#     t.lt(90)

#     t.fd(200)

#     t.lt(90)

#     t.fd(200)

#     t.lt(90)

#     t.fd(200)

#     t.lt(90)

#     t.rt(15)

# t.done()

