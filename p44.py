n=int(input())
l=list(map(int,input().split()))
maxx=l[0]
for i in l:
    if i>maxx:
        maxx=i
print(maxx)
minn=l[0]
for j in l:
    if j<minn:
        minn=j
print(minn)
