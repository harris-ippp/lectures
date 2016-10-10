def sum_for(n):

  s = 0
  for i in range(n+1): s += i
  return s


def sum_built_in(n):

  return sum(range(n+1))

  
def sum_constant(n):

  return int(n * (n+1) / 2)


N = int(1e9)
loops = 1

for i in range(loops):
  sf = sum_for(N)
  sb = sum_built_in(N)
  sc = sum_constant(N)


