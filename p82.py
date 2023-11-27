n=int(input())
A=[]
for i in range(0,n):
    l=list(map(int,input().split()))
    A.append(l)
pd=0
sd=0
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            pd=pd+A[i][j]
        if i+j==n-1:
            sd=sd+A[i][j]
print(pd-sd)
    
      
