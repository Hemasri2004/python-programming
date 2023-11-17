n=int(input())
l=list(map(int,input().split()))
maxx=l[-1]
minn=l[0]
for i in range(0,n):
    if i<maxx:
        i=maxx
    if i>minn:
        i=minn
print(minn,end=" ")
print(maxx)
    
