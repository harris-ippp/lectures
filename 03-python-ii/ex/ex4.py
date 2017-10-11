#!/usr/bin/env python 

# Just trust me on this for a moment.
from dogs import dog

# Modify the people class, to make the 
# greeting more dog-appropriate.
class person():

  def __init__(self, name): self.name = name

  def greet(self, other):

    if type(other) is person:
      print("How do you do, {}?".format(other.name))
      other.respond(self)

    if type(other) is dog:
      print("Who's a good boy?  Is {} a good boy?".format(other.name))
      other.happy_ears()

  def respond(self, other):
    
    print("Fabulous, thank you dear {}!".format(other.name))


c = person("Charles")
n = person("Nancy")
k = dog("Kaiser")

c.greet(n)
n.greet(c)
c.greet(k)


