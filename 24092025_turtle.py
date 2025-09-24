import turtle
turtle.Screen().bgcolor("Orange")
polygon = turtle.Turtle()
for i in range(6):
    polygon.forward(100)
    polygon.right(60)
turtle.done()


import turtle
turtle.Screen().bgcolor("Pink")
star = turtle.Turtle()
star.right(75)
star.forward(150)
for i in range(4):
    star.right(145)
    star.forward(150)
turtle.done()


import turtle
import random
turtle.Screen().bgcolor("Light Blue")
spiral = turtle.Turtle()
def draw():
    for i in range(150):
        spiral.color(random.random(),random.random(),random.random())
        spiral.forward(2*i)
        spiral.left(121)
spiral.penup()
spiral.goto(0,0)
spiral.pendown()
for i in range(6):
    spiral.penup()
    spiral.goto(random.randint(-300,300),random.randint(-300,300))
    spiral.pendown()
    draw()
turtle.done()