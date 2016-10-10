s = my_obj()
for x in range(N):
  s.const_fn(x)
  for y in range(N):
    s.const_fn(y)
    for z in range(N):
      s.const_fn(z)
