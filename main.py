from operator import le
import turtle
turtle.Screen().bgcolor("black")
t=turtle.Turtle()
t.color("#ffde40")

def turn():
    t.left(45)
    t.forward(6)
    t.left(45)

t.color("#498c0d")
t.pensize(9)
t.forward(170)
turn()
t.forward(85)
t.color("#ee8027")
t.forward(85)
turn()
t.forward(330)
turn()
t.forward(85)
t.color("#498c0d")
t.forward(85)
turn()
t.forward(170)


t.color("white")
t.pensize(14)

#b
t.penup()
t.backward(135)
t.left(90)
t.forward(140)
t.right(90)
t.pendown()
t.forward(45)
t.right(90)
t.forward(40)
t.right(45)
t.forward(8)
t.right(45)
t.forward(35)
t.left(90)
t.forward(8)
t.left(90)
t.forward(35)
t.right(45)
t.forward(8)
t.right(45)
t.forward(40)
t.right(90)
t.forward(45)
t.right(90)
t.forward(100)

#g
t.penup()
t.right(180)
t.forward(53)
t.left(90)
t.forward(103)
t.pendown()
t.forward(25)
t.right(90)
t.forward(45)
t.right(90)
t.forward(45)
t.right(90)
t.forward(95)
t.right(90)
t.forward(45)

#m
t.penup()
t.forward(40)
t.right(90)
t.forward(95)
t.left(180)
t.pendown()
t.forward(96)
t.right(150)
t.forward(55)
t.left(120)
t.forward(55)
t.setheading(0)
t.right(90)
t.forward(96)

#i
t.penup()
t.left(90)
t.forward(40)
t.left(90)
t.pendown()
t.forward(96)

turtle.done()
