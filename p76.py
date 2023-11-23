n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(1,m+1):
    first=l[0]
    for j in range(0,n-1):
        l[j]=l[j+1]
    l[n-1]=first
for i in l:
    print(i,end=" ")

