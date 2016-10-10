from random import randint

l, Nsq = [],  N*N
for i in range(N):
  l.append(randint(0, Nsq))

for a in range(N):
  idx = l.index(a)
  s.const_fn(idx, a)
