def prime(i):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
n=int(input())
l=[i for i in range(0,n+1) if prime(i)]
for i in l:
    print(i,end=" ")
