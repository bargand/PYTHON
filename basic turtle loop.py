import turtle

turtle.speed(100)

for i in range(160):

    for j in range (2):

       turtle.fd(i)

       turtle.lt(60)

       turtle.rt(120)

    turtle.rt(240)

    turtle.lt(51)

    turtle.circle(3)

turtle.done()