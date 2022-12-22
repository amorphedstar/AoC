with open('input8', 'r') as file:
  ls = [list(map(int,l)) for l in file.read().strip().split('\n')]
#   ls = [[3,0,3,7,3],
# [2,5,5,1,2],
# [6,5,3,3,2],
# [3,3,5,4,9],
# [3,5,3,9,0],
# ]
  m=len(ls)
  n=len(ls[0])
  g = [[0]*n for _ in ls]
  for i in range(m):
    bv = -1
    for j in range(n):
      if ls[i][j] <= bv:
        continue
      bv = ls[i][j]
      g[i][j] |= 1
  for i in range(m):
    bv = -1
    for j in range(n):
      if ls[i][~j] <= bv:
        continue
      bv = ls[i][~j]
      g[i][~j] |= 1
  
  for j in range(n):
    bv = -1
    for i in range(m):
      if ls[i][j] <= bv:
        continue
      bv = ls[i][j]
      g[i][j] |= 1
  for j in range(n):
    bv = -1
    for i in range(m):
      if ls[~i][j] <= bv:
        continue
      bv = ls[~i][j]
      g[~i][j] |= 1
  # print('\n'.join(''.join(map(str,r)) for r in g))
  print(sum(map(sum,g)))
  bss = 0
  for i in range(m):
    for j in range(n):
      a,b,c,d = [0]*4
      bv = ls[i][j]
      for ni in range(i+1,m):
        a += 1
        if ls[ni][j] >= bv:
          break
      for ni in range(i-1,-1,-1):
        b += 1
        if ls[ni][j] >= bv:
          break
      for nj in range(j+1,n):
        c += 1
        if ls[i][nj] >= bv:
          break
      for nj in range(j-1,-1,-1):
        d += 1
        if ls[i][nj] >= bv:
          break
      bss = max(bss,a*b*c*d)
  print(bss)
