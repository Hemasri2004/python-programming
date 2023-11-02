n=int(input())
l=list(map(int,input().split()))
minn=l[0]
for i in range(n):
   if(l[i]<minn):
        minn=l[i]
l.remove(minn)
minn=l[0]
for i in l:
   if i<minn:
      minn=i
print(minn)
