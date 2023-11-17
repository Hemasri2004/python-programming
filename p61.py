def large(l,k):
 l.sort(reverse=True)
 for i in range(0,k):
    print(l[i],end=" ")
    
n=int(input())
l=list(map(int,input().split()))
k=int(input())
large(l,k)
