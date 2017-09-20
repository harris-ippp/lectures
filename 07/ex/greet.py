def greet(request, w):

  return HttpResponse("Well hello, {}!".format(w))
