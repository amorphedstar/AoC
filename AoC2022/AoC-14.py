from collections import *
import numpy as np
from functools import *

with open('input14', 'r') as file:
  ls = [l.split(' -> ') for l in file.read().strip().split('\n')]# if l]
  pic = [[0]*1000 for _ in range(1000)]
  mxx = 0
  for r in ls:
    p1,p2 = None,None
    for vv in r:
      v1,v2 =  map(int,vv.split(','))
      if p1 or p2:
        if p1 == v1:
          d = 1 if v2>p2 else -1
          for x2 in range(p2,v2+d,d):
            pic[x2][v1] = 1
            mxx=max(mxx,x2)
        if p2 == v2:
          d = 1 if v1>p1 else -1
          for x1 in range(p1,v1+d,d):
            pic[v2][x1] = 1
            mxx=max(mxx,v2)
      p1,p2 = v1,v2
  sx,sy = 0,500
  ct = 0
  pic[mxx+2] = [1]*1000
  mct = 0
  while not pic[sx][sy]:
    cx,cy = sx,sy
    brk = False
    while True:
      if cx > mxx and not mct:
        mct = ct
      if pic[cx+1][cy]==0:
        cx += 1
      elif pic[cx+1][cy-1]==0:
        cx += 1
        cy -= 1
      elif pic[cx+1][cy+1]==0:
        cx += 1
        cy += 1
      else:
        pic[cx][cy] = 1
        break
    ct += 1
  print(mct)
  print(ct)