def get_reader(request): # note: no other params.

  # if we knew the parameters...
  # state = request.GET.get('state', '')

  d = dict(request.GET._iterlists())
  return HttpResponse(str(d))
