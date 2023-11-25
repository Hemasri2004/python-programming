n=int(input())
A=[]
for i in range(n):
    l=list(map(int,input().split()))
    A.append(l)
for i in range(0,n):
    csum=0
    for j in range(0,n):
        csum=csum+A[j][i]
    print(csum,end=' ')
        
