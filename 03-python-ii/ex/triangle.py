#!/usr/bin/env python 

import turtle

t = turtle.Turtle()

turtle.delay(0)
turtle.tracer(10)
turtle.colormode(1)

t.width(1)
t.pencolor(0, 0, 0)
t.fillcolor(1, 0, 0)

size = 10
for x in range(300):
  size *= 1.02
  t.fd(size)
  t.right(123)

turtle.getscreen().getcanvas().postscript(file="triangle.eps")
input("done?")

