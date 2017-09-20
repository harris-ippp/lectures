#!/usr/bin/env python 

import math
import turtle 

turtle.tracer(0, 0)

t = turtle.Turtle()


def square(t, d = 100): 
  
  for i in range(4):
    t.fd(d)
    t.left(90)

def polygon(t, dist = 100, sides = 4, color = 0): 
  
  t.width(0)
  t.color(color, color, color)
  t.begin_fill()
  for i in range(sides):
    t.fd(dist)
    t.right(360/sides)    
  t.end_fill()

t.right(90)
t.fd(40)
for n in range(3):
  for d in range(1, 21):
    polygon(t, (20 - d) * 8, 6, d/20)
  t.right(120)

turtle.update()

turtle.getscreen().getcanvas().postscript(file="polygon.eps")

input("hold")

