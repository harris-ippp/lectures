#!/usr/bin/env python 

import turtle
from math import pi, cos, sin, atan2, sqrt
import math


nsteps = 100

# set these to 0, to help you debug
turtle.delay(0)
turtle.tracer(0)


def spiro_color(frac, colA, colB):

  if frac < 0: frac = 0
  if frac > 1: frac = 1
  
  col = []
  for a, b in zip(colA, colB):
    col.append(a * frac + b * (1 - frac))

  return col

# ring_rad = 300, disk_rad = 125, hole_rad = 100
def spirograph(R = 300, r_fr = 125/300, h_fr = 100/125, col1 = (1, 0, 0), col2 = (1, 0, 0)):

  # create two turtle objects.
  a = turtle.Turtle()
  b = turtle.Turtle()
  
  # Move the turtles to their starting positions,
  # with their pens up.  Use radians.
  # The "wheel" turtle will be hidden.
  a.radians()
  a.penup()
  a.fd(R * (1 - r_fr))
  a.left(pi/2)
  a.ht()
  
  # Move the turtles to their starting positions,
  # with their pens up.  Use radians.
  b.radians()
  b.penup()
  b.width(2)
  b.fd(R * (1 - r_fr * (1 - h_fr)))
  b.pendown()
  b.ht()
  
  nloops = 200
  for loop in range(nloops):
    if ((loop+1) * (1 - r_fr)/r_fr) % 1 < 1e-5:
      nloops = loop + 2
      break


  th = 0 # wheel angle.

  for loop in range(nloops):
    for step in range(nsteps):

      a.fd(2 * R * (1 - r_fr) * pi / nsteps)
      a.left(2 * pi / nsteps) # turn for next time.
  
      # keep track of the angular position of the large circle.
      # we actually need the full angle, not just mod 2pi,
      # since we are multiplying this by a funky fraction.
      # (In other words, we can't just as the big turtle what
      #  his angle is.)
      th += 2 * pi / nsteps
  
      # get the wheel's position 
      ax, ay = a.pos()
      bx = ax + R * r_fr * h_fr * cos(- th * (1 - r_fr)/r_fr)
      by = ay + R * r_fr * h_fr * sin(- th * (1 - r_fr)/r_fr)

      # make a cool, radius-dependent coloring scheme.
      # colors are denoted by fractions of R, G, B.
      # create a function 
      fade = (b.distance(0, 0) - R * (1 - r_fr)) / (r_fr * R)
      b.pencolor(spiro_color(fade, col1, col2))

      # now go to the new position.
      b.setpos(bx, by)

  
# now run several spirographs
# spirograph(R = 300, r_fr = 0.74, h_fr = 0.8, col1 = (0, 1, 1), col2 = (0, 0, 1))
# spirograph(R = 105, r_fr = 0.35, h_fr = 0.4, col1 = (1, 0, 0), col2 = (1, 1, 0))
# spirograph(R = 40,  r_fr = 0.45, h_fr = 0.9, col1 = (0, 1, 0), col2 = (0, 0, 1))

blue, green = (0, 0, 1), (0, 1, 1)
for x in range(11):
  col = spiro_color(x * 0.1, green, blue)
  spirograph(R = 300, r_fr = 0.5 + 1/12, h_fr = 0.7 - x * 0.05, col1 = col, col2 = col)
input("Hold")

turtle.getscreen().getcanvas().postscript(file="spirograph.eps")


