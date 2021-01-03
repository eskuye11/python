import turtle as t
import random


me = t.Turtle("turtle")
t.colormode(255)
me.pensize(10)
screens = t.Screen()
screens.setup(width=940, height=400)
screens.title("      Let's ride the Python's Train ! ")
screens.bgcolor('black')
me.penup()
me.goto(x=-380, y=-35)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


me.pendown()
me.left(90)
me.color(random_color())
me.forward(185)
me.right(90)
me.color(random_color())
me.forward(60)
me.right(90)
me.color(random_color())
me.forward(80)               # xx
me.right(90)
me.color(random_color())
me.forward(60)
me.penup()              # p


me.goto(x=-285, y=0)
me.right(110)
me.pendown()
me.color(random_color())
me.forward(165)
me.left(180)
me.color(random_color())
me.forward(80)
me.right(135)
me.color(random_color())
me.forward(80)
me.penup()                          # Y


me.goto(x=-155, y=0)
me.pendown()
me.right(25)
me.color(random_color())
me.forward(150)
me.left(90)
me.color(random_color())
me.forward(50)
me.right(180)
me.color(random_color())
me.forward(100)
me.penup()                 # T


me.goto(x=-60, y=0)
me.pendown()
me.left(90)
me.color(random_color())
me.forward(150)
me.right(180)
me.color(random_color())
me.forward(70)
me.left(90)
me.color(random_color())
me.forward(60)
me.left(90)
me.color(random_color())
me.forward(70)
me.right(180)
me.color(random_color())
me.forward(150)
me.penup()                # H


me.goto(x=100, y=0)
me.left(90)
me.pendown()
me.color(random_color())
me.circle(75)
me.penup()                   # O

me.goto(x=210, y=0)
me.pendown()
me.left(90)
me.color(random_color())
me.forward(150)
me.goto(x=300, y=0)
me.color(random_color())
me.forward(150)                  # N
me.penup()


me.goto(x=210, y=-10)
me.pendown()
me.goto(x=-285, y=-10)
me.left(90)
me.color(random_color())
me.left(90)                 # <-----


me.forward(15)
me.left(90)
me.pensize(2)
me.forward(630)      # |
me.pensize(10)

me.left(90)
me.color(random_color())
me.forward(35)
#
me.right(180)
me.forward(60)
me.right(90)      # <--------
me.forward(680)

me.right(90)
me.forward(25)
#                                  thin line
me.pensize(2)
me.left(90)
me.color(random_color())
me.forward(5)
for x in range(180):
    me.forward(1)
    me.left(1)

me.forward(50)
me.color(random_color())
for x in range(6):
    me.circle(20)
    me.penup()
    me.forward(20)
    me.color(random_color())
    me.pendown()
me.back(10)
me.forward(360)
me.color(random_color())
for x in range(6):
    me.circle(20)
    me.penup()
    me.forward(20)
    me.color(random_color())
    me.pendown()


me.back(10)
me.color(random_color())
me.forward(60)
me.color(random_color())
for x in range(180):
    me.forward(1)
    me.left(1)

me.penup()

me.goto(x=100, y=75)
for y in range(5):
    me.circle(20)
me.right(90)


screens.exitonclick()








