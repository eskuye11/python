import turtle as t
import random


me = t.Turtle()
t.colormode(255)
me.speed('fastest')
me.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        me.color(random_color())
        me.circle(100)
        me.setheading(me.heading() + gap_size)



spirograph(5)
screens = t.Screen()
screens.exitonclick()


