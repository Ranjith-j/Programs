n=int(input())
a=list(map(int,input().split()))
dup=list(set(a));co=0
for i in dup:
  if a.count(i)>1:co+=1
print("unique" if co==0 else co)
