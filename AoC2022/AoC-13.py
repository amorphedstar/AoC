from collections import *
import numpy as np
from functools import *

def leq(v1,v2):
  if type(v1) is list and type(v2) is int:
    v2 = [v2]
  if type(v2) is list and type(v1) is int:
    v1 = [v1]
  if type(v1) is int and type(v2) is int:
    return (v1 < v2, v1 <= v2)
  n1=len(v1)
  n2=len(v2)
  for i in range(n1):
    if i >= n2:
      return (False,False)
    cc = leq(v1[i],v2[i])
    if cc[0]: return (True,True)
    if not cc[1]:
      return (False,False)
  return (n2>n1,True)

with open('input13', 'r') as file:
  ls = [eval(l) for l in file.read().strip().split('\n') if l]
#   ls = [eval(l) for l in '''[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]
# '''.strip().split() if l]
  a=0
  n = len(ls)//2
  div1 = [[2]]
  div2 = [[6]]
  for i in range(n):
    l1,l2 = ls[i*2:i*2+2]
    cmp = leq(l1,l2)[1]
    if cmp:
      a += i+1
  print(a)
  ls.append(div2)
  ls.append(div1)
  ls.sort(key=cmp_to_key(lambda x,y:1 if not leq(x,y)[1] else -1))
  print((ls.index(div1)+1)*(ls.index(div2)+1))
