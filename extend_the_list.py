a=[];n=int(input())
for x in range(n):
  h=int(input())
  li=[int(i) for i in input().split()]
  li.sort()
  a.extend(li[:h])
print(*a)
