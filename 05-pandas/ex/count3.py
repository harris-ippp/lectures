def my_fn(s, N):
  while N:
    N //= 2
    s.const_fn(N)

s = my_obj()
for x in range(N):
  my_fn(s, N)
