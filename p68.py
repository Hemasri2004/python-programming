n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):#outerloop 
    count=0
    for j in range(0,n):#innerloop
        if l[i]==l[j]:
            count=count+1#
    if count==1:
        print(l[i],end=' ')
        
