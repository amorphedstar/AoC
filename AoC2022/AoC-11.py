from collections import defaultdict


with open('input11', 'r') as file:
  ls = [l for l in file.read().strip().split('\n')]
  ds = [[] for _ in range(8)]
  fs = [lambda x: x*5, lambda x: x+6, lambda x: x+5, lambda x: x+2, lambda x: x*7, lambda x: x+7, lambda x: x+1, lambda x: x*x]
  divs = [3,17,2,19,11,5,13,7]
  arrs = [(7,4),(3,0),(3,1),(7,0),(5,6),(2,1),(5,2),(4,6)]
  for i in range(8):
    rws = ls[i*7:i*7+7]
    for v in map(lambda x: int(x.replace(',','')),rws[1].strip().split()[2:]):
      ds[i].append(v)
  cts = [0]*8
  for _ in range(20):
    for i in range(8):
      for v in ds[i]:
        cts[i] += 1
        n = fs[i](v)
        n //= 3
        if n%divs[i] == 0:
          ds[arrs[i][0]].append(n)
        else:
          ds[arrs[i][1]].append(n)
      ds[i] = []
  cts.sort()
  print(cts[-1]*cts[-2])

from collections import defaultdict


with open('input11', 'r') as file:
  ls = [l for l in file.read().strip().split('\n')]
  ds = [[] for _ in range(8)]
  fs = [lambda x: x*5, lambda x: x+6, lambda x: x+5, lambda x: x+2, lambda x: x*7, lambda x: x+7, lambda x: x+1, lambda x: x*x]
  divs = [3,17,2,19,11,5,13,7]
  prod = 3*17*2*19*11*5*13*7
  arrs = [(7,4),(3,0),(3,1),(7,0),(5,6),(2,1),(5,2),(4,6)]
  for i in range(8):
    rws = ls[i*7:i*7+7]
    for v in map(lambda x: int(x.replace(',','')),rws[1].strip().split()[2:]):
      ds[i].append(v)
  cts = [0]*8
  for _ in range(10000):
    for i in range(8):
      for v in ds[i]:
        cts[i] += 1
        n = fs[i](v)
        n %= prod
        if n%divs[i] == 0:
          ds[arrs[i][0]].append(n)
        else:
          ds[arrs[i][1]].append(n)
      ds[i] = []
  cts.sort()
  print(cts[-1]*cts[-2])