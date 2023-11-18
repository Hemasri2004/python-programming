k=[]
n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(0,n):
    k=l[i]+m[i]
    print(k,end=" ")
