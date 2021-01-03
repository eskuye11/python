import turtle as t
import random


me = t.Turtle()
t.colormode(255)
me.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def differentAngles(n):
    angle = 360 / n
    for x in range(n):
        me.forward(100)
        me.right(angle)
        me.color(random_color())


me.left(90)
me.penup()
me.forward(130)
me.left(90)
me.forward(58)
me.right(180)
me.pendown()

for shape_of in range(3, 10):
    differentAngles(shape_of)
    # me.color(random_color())



screens = t.Screen()
screens.exitonclick()