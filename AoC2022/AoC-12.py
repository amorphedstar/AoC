from collections import defaultdict, deque


with open('input12', 'r') as file:
  ls = [list(l) for l in file.read().strip().split('\n')]
#   ls = [list(l) for l in """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# """.strip().split('\n')]
  ns = [[float('inf')]*len(ls[0]) for v in ls]
  m,n = len(ls),len(ls[0])
  for i in range(m):
    for j in range(n):
      if ls[i][j] == 'S':
        si = i
        sj = j
        ls[i][j] = 'a'
      if ls[i][j] == 'E':
        ei = i
        ej = j
        ls[i][j] = 'z'
  ns[si][sj] = 0
  q = deque([(si,sj)])
  while q:
    i,j = q.popleft()
    for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
      ni,nj = i+di,j+dj
      if 0 <= ni < m and 0 <= nj < n:
        if ns[ni][nj] != float('inf'): continue
        v1,v2 = ord(ls[i][j]),ord(ls[ni][nj])
        if v2 <= v1 + 1:
          ns[ni][nj] = ns[i][j] + 1
          q.append((ni,nj))
  # print(ns)
  print(ns[ei][ej])

from collections import defaultdict, deque


with open('input12', 'r') as file:
  ls = [list(l) for l in file.read().strip().split('\n')]
#   ls = [list(l) for l in """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# """.strip().split('\n')]
  ns = [[float('inf')]*len(ls[0]) for v in ls]
  m,n = len(ls),len(ls[0])
  for i in range(m):
    for j in range(n):
      if ls[i][j] == 'S':
        si = i
        sj = j
        ls[i][j] = 'a'
      if ls[i][j] == 'E':
        ei = i
        ej = j
        ls[i][j] = 'z'
  ns[ei][ej] = 0
  q = deque([(ei,ej)])
  while q:
    i,j = q.popleft()
    if ls[i][j] == 'a':
      print(ns[i][j])
      break
    for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
      ni,nj = i+di,j+dj
      if 0 <= ni < m and 0 <= nj < n:
        if ns[ni][nj] != float('inf'): continue
        v1,v2 = ord(ls[i][j]),ord(ls[ni][nj])
        if v2 >= v1 - 1:
          ns[ni][nj] = ns[i][j] + 1
          q.append((ni,nj))
  # print(ns)
  # print(ns[ei][ej])