from collections import defaultdict


with open('input7', 'r') as file:
  l = [ls for ls in file.read().strip().split('\n')]
  stk = ['init']
  dct = defaultdict(int)
  pc = defaultdict(int)
  dd = defaultdict(list)
  ptr = {}
  cp = ''
  for ls in l[1:]:
    if ls[0] == '$':
      ls = ls[2:]
      if ls[:2]=='cd':
        nd = ls[3:]
        if nd == '..':
          stk.pop()
        else:
          stk.append(nd)
      elif ls[:2] == 'ls':
        cp = '/'.join(stk)
        dct[cp] = 0
    else:
      qt, nm = ls.split()
      if qt == 'dir':
        pc[cp] += 1
      else:
        dct[cp] += int(qt)
  done = set()
  dirnms = dct.keys()
  def rec(nm):
    if nm in done: return
    if pc[nm]: return
    done.add(nm)
    splt = nm.split('/')
    if len(splt) == 1: return
    pc['/'.join(splt[:-1])] -= 1
    dct['/'.join(splt[:-1])] += dct[nm]
    if not pc['/'.join(splt[:-1])]:
      rec('/'.join(splt[:-1]))
  for nm in dirnms:
    rec(nm)
  print(sum([v for k,v in dct.items() if v<=100000]))
  uu = 70000000 - dct['init']
  print(min([v for k,v in dct.items() if uu+v >= 30000000]))