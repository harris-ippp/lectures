#!/usr/bin/env python

import turtle
import math

a = turtle.Turtle()

turtle.delay(0)
turtle.tracer(0)
turtle.colormode(1)

a.width(0)
a.pencolor(0, 0, 0)
a.fillcolor(1, 0, 0)

for t in range(90):
 a.pencolor(t/90, t/90, t/90)
 a.fillcolor(t/90, t/90, t/90)
 a.begin_fill()
 a.circle(120 * math.exp(-t/45))
 a.right(32)
 a.end_fill()

cv = a.screen.getcanvas()

input("All done?")

