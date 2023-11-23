n=int(input())
l=list(map(int,input().split()))
r,e=map(int,input().split())
for i in range(r+1,e+1):
    first=l[r]
    for j in range(r,e):
        l[j]=l[j+1]
    l[e]=first
for i in l:
    print(i,end=" ")
