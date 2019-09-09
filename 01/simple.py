from turtle import *
from math import *

from config import *

l, h = 300, 350

t = 0  # time
xk, yk = 0, 0  # position in time

v, a = force, radians(angle)  # velocity and angle


# draw objective


def draw_objective():
    penup()
    speed('fastest')
    goto((l, 0))
    pendown()
    pencolor('red')
    goto((h, 0))


# draw travel


def draw_travel():
    global xk, yk, t
    penup()
    speed('fastest')
    goto((0, 0))
    pendown()
    speed('normal')
    pencolor('black')

    shape('circle')
    shapesize(0.2, 0.2)

    while yk >= 0:
        xk = v * t * cos(a)
        yk = v * t * sin(a) - 1/2 * 9.8 * t**2
        goto((xk, yk))
        print(pos())
        t += 0.1


setworldcoordinates(0, 0, 500, 500)

width(2)
draw_objective()
draw_travel()

if l <= xk <= h:
    print('You won!')
else:
    print('You loose')

print('Click on the turtle screen to close it.')
exitonclick()
