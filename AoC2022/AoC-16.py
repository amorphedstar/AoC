from collections import *
import numpy as np
from functools import *

with open('input', 'r') as file:
  ls = [l for l in file.read().strip().split('\n')]
  ls = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
""".strip().split('\n')
  g = defaultdict(list)
  qs = defaultdict(int)
  a = []
  for l in ls:
    lsp = l.split()
    v = lsp[1]
    q = int(lsp[4][5:-1])
    t = [s[:2] for s in lsp[9:]]
    g[v] = t
    qs[v]=q
  lst = deque()
  for v in g:
    lst.append((0,v,set(),0,0))
  bsf = {}
  a=0
  while lst:
    t,v,o,r,s = lst.popleft()
    if t == 19:
      a=max(a,r)
      continue
    # print('h')
    if v not in o:
      lst.append((t+1,v,o.union([v]),r+s,s+qs[v]))
    for nn in g[v]:
      lst.append((t+1,nn,o,r+s,s))
    # print(lst)
  # print(g)
  # print(qs)
  print(a)