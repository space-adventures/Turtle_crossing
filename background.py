import turtle

def yellow_line():
    tim = turtle.Turtle()
    tim.ht()
    tim.pensize(10)
    tim.pencolor('gold')
    tim.goto(300, 0)
    tim.lt(180)
    for i in range(30):
        tim.fd(20)

def white_line(location):
    tim = turtle.Turtle()
    tim.ht()
    tim.pensize(10)
    tim.pencolor('white')
    tim.pu()
    tim.goto(300, location)
    tim.lt(180)
    for i in range(30):
        tim.pd()
        tim.fd(20)
        tim.pu()
        tim.fd(20)
