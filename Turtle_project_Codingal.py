import turtle
turtle.Screen().bgcolor("cyan")
square = turtle.Turtle()
x = 60
a = 10
b = -10
for d in range(6):
    for i in range(4):
        square.left(90)
        square.forward(x)
    square.penup()
    square.goto(a, b)
    square.pendown()
    x += 20
    a += 10
    b -= 10
turtle.done()