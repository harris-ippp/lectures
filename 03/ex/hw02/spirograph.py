#!/usr/bin/env python 

import turtle
from math import pi, cos, sin, atan2, sqrt
import math


# this will affect the fine-ness of the loops.
nsteps = 40

# create two turtle objects.
a = turtle.Turtle()
a.radians()

b = turtle.Turtle()
b.radians()


# set these to 0, to help you debug
turtle.delay(0)
turtle.tracer(0)


def spirograph(ring_rad = 300, disk_rad = 125, hole_rad = 100):

  # Move the turtles to their starting positions,
  # with their pens up.  Use radians.
  # The "wheel" turtle will be hidden.
  a.penup()
  a.fd(ring_rad - disk_rad)
  a.left(pi/2)
  a.ht()
  
  # Move the turtles to their starting positions,
  # with their pens up.  Use radians.
  b.penup()
  b.width(2)
  b.fd(ring_rad - disk_rad + hole_rad)
  b.pendown()
  b.ht()
  
  # CHALLENGE:
  # figure out how many loops you need, 
  # for the parameters given
  nloops = 200 

  th = 0 # wheel angle.

  for loop in range(nloops):
    for step in range(nsteps):

      # Turle a should performe one circle every loop.
      # Use fd/bk/left/right  commands to achieve that.
      a.fd(2 * (ring_rad - disk_rad) * pi / nsteps)
      a.left(2 * pi / nsteps) # turn for next time.
  
      # keep track of the angular position of the large circle.
      # we actually need the full angle, not just mod 2pi,
      # since we are multiplying this by a funky fraction.
      # (In other words, we can't just as the big turtle what
      #  his angle is.)
      th += 2 * pi / nsteps
  
      # get the wheel's position 
      ax, ay = a.pos()

      # use that position,
      # along with the sine/cosine from the assignment
      # to find the destination bx, by of the _hole_ turtle (b).
      bx = ax + hole_rad * cos(- th * (ring_rad - disk_rad)/disk_rad)
      by = ay + hole_rad * sin(- th * (ring_rad - disk_rad)/disk_rad)

      # CHALLENGE: create a function to make a cool
      # radius or time-dependent color scheme.
      # colors are denoted by fractions of R, G, B.

      # now go to the new position.
      b.setpos(bx, by)

  
# At least one call -- but get creative!!
spirograph()

# Leave this here to print your pretty picture.
turtle.getscreen().getcanvas().postscript(file="spirograph.eps")


