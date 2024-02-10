n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
for i in d:
    if d[i]>1:
        print(i,end=" ")
