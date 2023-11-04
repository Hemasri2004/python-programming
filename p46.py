num=list(map(int,input().split()))
n=len(num)
print(n*(n+1)//2-sum(num))
