n=int(input())
li=[int(i) for i in input().split()]
a,b=map(int,input().split())
print(abs(li[:n].index(a)-li[:n].index(b)))
