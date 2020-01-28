n=int(input())
lis=list(map(int,input().split()))
fact_list=[]
for i in lis[:n]:
    fact=1
    for x in range(1,i+1):
        fact*=x
    fact_list+=[fact]
print(*fact_list)
    
