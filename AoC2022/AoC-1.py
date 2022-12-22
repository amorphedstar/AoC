with open('input1', 'r') as file:
  print(max([sum(list(map(int,ls.split()))) for ls in file.read().split('\n\n')]))
with open('input1', 'r') as file:
  print(sum(sorted([sum(list(map(int,ls.split()))) for ls in file.read().split('\n\n')])[-3:]))