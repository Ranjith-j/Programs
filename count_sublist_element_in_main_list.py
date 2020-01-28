n=int(input())
l1=[int(i) for i in input().split()]
m=int(input())
l2=[int(i) for i in input().split()]
for i in range(m):
  if l1[:n].count(l2[i])==0:
    print("Not Present",end=" ")
  else:
    print(l1[:n].count(l2[i]),end=" ")

