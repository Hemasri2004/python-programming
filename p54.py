l=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    l.append(x)
minn=l[0]
maxx=l[0]
for j in range(0,n):
    if(l[j]>maxx):
        maxx=l[j]
    if(l[j]<minn):
        minn=l[j]
print(maxx)
print(minn)
