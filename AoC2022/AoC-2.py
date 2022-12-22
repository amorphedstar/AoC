with open('input2', 'r') as file:
  prs = [ls.split() for ls in file.read().strip().split('\n')]
  # prs = [['A','Y'],['B','X'],['C','Z']]  
  ans = 0
  for a,x in prs:
    v1,v2 = ord(a)-ord('A'), ord(x)-ord('X')
    ws = (v2-v1+1)%3
    ans += 3*ws+v2+1
  print(ans)
with open('input2', 'r') as file:
  prs = [ls.split() for ls in file.read().strip().split('\n')]
  # prs = [['A','Y'],['B','X'],['C','Z']]
  ans = 0
  for a,x in prs:
    v1,v2 = ord(a)-ord('A'), ord(x)-ord('X')
    c = (v1+v2-1)%3
    ans += 3*v2+c+1
  print(ans)
