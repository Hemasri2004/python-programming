n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    for j in range(i+1,n):
            if l[i]==l[j]:
                print(l[j],end=' ')
                break
   
