n=int(input())
l=list(map(int,input().split()))
fmin=min(l)
l.remove(fmin)
smin=min(l)
print(smin)
