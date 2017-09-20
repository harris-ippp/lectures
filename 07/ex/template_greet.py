from django.shortcuts import render

def greet_template(req, w): 
  return render(req, "greet.html", {'who' : w})
