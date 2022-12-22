with open('input3', 'r') as file:
  l = [ls for ls in file.read().strip().split('\n')]
#   l = ['vJrwpWtwJgWrhcsFMMfFFhFp',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
# 'ttgJtRGJQctTZtZT',
# 'CrZsJsPPZsGzwwsLwLmpwMDw'
# ]  
  ans = 0
  for ls in l:
    s1,s2 = (ls[:len(ls)//2],ls[len(ls)//2:])
    s1,s2 = set(s1), set(s2)
    c = list(s1.intersection(s2))[0]
    if ord(c)>=97:
      ans += ord(c)-96
    else:
      ans += 26+ord(c)-64
  print(ans)
with open('input3', 'r') as file:
  l = [ls for ls in file.read().strip().split('\n')]
#   l = ['vJrwpWtwJgWrhcsFMMfFFhFp',
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
# 'ttgJtRGJQctTZtZT',
# 'CrZsJsPPZsGzwwsLwLmpwMDw'
# ]  
  ans = 0
  for i in range(len(l)//3):
    l1,l2,l3 = l[3*i:3*i+3]
    s1,s2,s3 = map(set,[l1,l2,l3])
    c = list(s1.intersection(s2&s3))[0]
    if ord(c)>=97:
      ans += ord(c)-96
    else:
      ans += 26+ord(c)-64
  print(ans)
