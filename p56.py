n=int(input())
l=list(map(int,input().split()))
osum=0
asum=0
osum=n*(n+1)//2
asum=sum(l)
print(osum-asum)

