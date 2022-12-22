from collections import defaultdict


with open('input9', 'r') as file:
  ls = [l for l in file.read().strip().split('\n')]
  vis = set()
  vis.add((0,0))
  dd = defaultdict(int)
  hx=hy=tx=ty=0
  def dr(dx,dy):
    global hx,hy,tx,ty
    cdx,cdy = hx-tx,hy-ty
    if cdx and cdy:
      if dx == cdx or dy == cdy:
        tx = hx
        ty = hy
    elif cdx:
      if dx == cdx:
        tx = hx
    elif cdy:
      if dy == cdy:
        ty = hy
    vis.add((tx,ty))
    hx += dx
    hy += dy

  for l in ls:
    d,n = l.split()
    n = int(n)
    if d == 'R':
      for _ in range(n):
        dr(1,0)
    if d == 'L':
      for _ in range(n):
        dr(-1,0)
    if d == 'U':
      for _ in range(n):
        dr(0,1)
    if d == 'D':
      for _ in range(n):
        dr(0,-1)
  print(len(vis))

from collections import defaultdict


with open('input9', 'r') as file:
  ls = [l for l in file.read().strip().split('\n')]
  vis = set()
  vis.add((0,0))
  dd = defaultdict(int)
  # hx=hy=tx=ty=0
  pos=[(0,0) for _ in range(11)]
  def dr(dx,dy,idx):
    hx,hy = pos[idx]
    tx,ty = pos[idx+1]
    nx,ny = hx+dx,hy+dy
    pos[idx]=(nx,ny)
    if abs(nx-tx) <= 1 and abs(ny-ty) <= 1:
      return

    if abs(nx-tx)==2:
      ntx = (nx+tx)//2
    else:
      ntx = nx
    if abs(ny-ty)==2:
      nty = (ny+ty)//2
    else:
      nty = ny

    if idx < 9:
      dr(ntx-tx,nty-ty,idx+1)

  for l in ls:
    d,n = l.split()
    n = int(n)
    if d == 'R':
      for _ in range(n):
        dr(1,0,0)
        vis.add(pos[9])
    if d == 'L':
      for _ in range(n):
        dr(-1,0,0)
        vis.add(pos[9])
    if d == 'U':
      for _ in range(n):
        dr(0,1,0)
        vis.add(pos[9])
    if d == 'D':
      for _ in range(n):
        dr(0,-1,0)
        vis.add(pos[9])
  print(len(vis))
