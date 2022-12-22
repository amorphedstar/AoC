with open('input4', 'r') as file:
  l = [ls for ls in file.read().strip().split('\n')]
  ans = 0
  for ls in l:
    c1,c2 = ls.split(',')
    c10,c11 = map(int,c1.split('-'))
    c20,c21 = map(int,c2.split('-'))
    if c10 <= c20 and  c21 <= c11 or c20 <= c10 and c11<= c21:
      ans += 1
  print(ans)
with open('input4', 'r') as file:
  l = [ls for ls in file.read().strip().split('\n')]
  ans = 0
  for ls in l:
    c1,c2 = ls.split(',')
    c10,c11 = map(int,c1.split('-'))
    c20,c21 = map(int,c2.split('-'))
    if c11 >= c20 and c21 >= c10 or c21 >= c10 and c11 >= c20:
      ans += 1
  print(ans)
