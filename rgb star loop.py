import turtle

colour = ['yellow' ,'green','red','white','cyan','blue']



t = turtle.Turtle()

screen = turtle.Screen()

screen.bgcolor('Black')

t.speed(30)



for i in range (100):

    t.color(colour[i%6])

    t.fd(i*5)

    t.left(200)

    t.width(2)
turtle.done()