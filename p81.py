n=int(input())
A=[]
for i in range(n):
    l=list(map(int,input().split()))
    A.append(l)
for i in range(0,n):    
    for j in range(0,n):
        cmax=A[i][0]
        if A[i][j]>cmax:
            cmax=A[i][j]
    print(cmax,end=' ')
    
