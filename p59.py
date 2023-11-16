n=int(input())
l=list(map(int,input().split()))
m=max(l)
for i in range(1,m):
    if i in l:
       continue
    else:
        print(i,end=" ")
