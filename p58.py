n=int(input())
l=list(map(int,input().split()))
fmax=max(l)
l.remove(fmax)
smax=max(l)
print(smax)
