with open('input5', 'r') as file:
  l = [ls for ls in file.read().strip().split('\n')]
  ss = l[:8]
  ols = l[10:]
  arrs = [[] for _ in range(9)]
  for i in range(7,-1,-1):
    for k in range(9):
      c = ss[i][4*k+1]
      if c != ' ':
        arrs[k].append(c)
  for s in ols:
    _,q,_,f,_,t = s.split()
    q,f,t = map(int,[q,f,t])
    f -= 1
    t -= 1
    for _ in range(q):
      arrs[t].append(arrs[f].pop())

  print(''.join(arr[-1] for arr in arrs))
with open('input5', 'r') as file:
  l = [ls for ls in file.read().strip().split('\n')]
  ss = l[:8]
  ols = l[10:]
  arrs = [[] for _ in range(9)]
  for i in range(7,-1,-1):
    for k in range(9):
      c = ss[i][4*k+1]
      if c != ' ':
        arrs[k].append(c)
  for s in ols:
    _,q,_,f,_,t = s.split()
    q,f,t = map(int,[q,f,t])
    f -= 1
    t -= 1
    arrs[t]+= arrs[f][-q:]
    for _ in range(q):
      arrs[f].pop()
    

  print(''.join(arr[-1] for arr in arrs))
