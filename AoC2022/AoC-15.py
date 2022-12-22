from collections import *
import numpy as np
from functools import *

with open('input15', 'r') as file:
  ls = [l for l in file.read().strip().split('\n')]
#   ls = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3
# """.strip().split('\n')
  arr = defaultdict(int)
  ect = defaultdict(int)
  imp = set()
  bcns = []
  css = []
  for l in ls:
    _,_,cx,cy,_,_,_,_,sx,sy = l.split()
    cx = int(cx[2:-1])
    cy = int(cy[2:-1])
    sx = int(sx[2:-1])
    sy = int(sy[2:])
    css.append((cx,cy,sx,sy))
    dst = abs(cx-sx)+abs(cy-sy)
    for x in range(cx-dst-1,cx+dst+2):
      dx = abs(x-cx)
      tup = (x,cy-dst-1+dx)
      ect[tup] += 1
      if ect[tup] == 4 and 0 <= tup[0] <= 4000000 and 0 <= tup[1] <= 4000000:
        imp.add(tup)
    for x in range(cx-dst,cx+dst+1):
      dx = abs(x-cx)
      tup = (x,cy+dst+1-dx)
      ect[tup] += 1
      if ect[tup] == 4 and 0 <= tup[0] <= 4000000 and 0 <= tup[1] <= 4000000:
        imp.add(tup)
    y = 2000000
    if sy == y:
      bcns.append(sx)
    df = abs(cy-y)
    df = dst-df
    if df >= 0:
      for i in range(cx-df,cx+df+1):
        arr[i] = 1
  # print(arr)
  for bcn in bcns:
    arr[bcn] = 0
  print(sum(arr.values()))
  print(len(imp))
  for x,y in imp:
    poss = True
    for cx,cy,sx,sy in css:
      if abs(cx-x)+abs(cy-y) <= abs(sx-cx)+abs(sy-cy):
        poss = False
        break
    if poss:
      print(x,y)
      print(x*4000000+y)
      # break