#Code for Etch-A-Sketch project
#w to move forward, s to move back, a to turn anticlockwise and d to turn clockwise
#Note that c clears everything

from turtle import Turtle, Screen
my_turt = Turtle()
screen = Screen()

def w_fd():
    my_turt.fd(10)


def s_bc(): 
    my_turt.backward(10)


def d_clock():
    my_turt.setheading(my_turt.heading()+ 10)


def a_anti():
    my_turt.setheading(my_turt.heading()- 10)

def c_clear():
    my_turt.clear() 
    my_turt.penup()
    my_turt.home()
    my_turt.pendown()

screen.listen()
screen.onkey(key= "W", fun= w_fd)
screen.onkey(key= "w", fun=w_fd )
screen.onkey(key= "s", fun= s_bc)
screen.onkey(key= "S", fun= s_bc)
screen.onkey(key="d"    , fun= d_clock)
screen.onkey(key = "D", fun= d_clock)
screen.onkey(key="a", fun= a_anti)
screen.onkey(key= "A", fun= a_anti)
screen.onkey(key= "c", fun= c_clear)
screen.onkey(key="C",fun= c_clear)

screen.exitonclick()  
