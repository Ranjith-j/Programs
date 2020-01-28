n=int(input())
lis=list(map(int,input().split()))
for i in lis[:n]:
    print("EVEN" if i%2==0 else "ODD")
