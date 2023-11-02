n=int(input())
l=list(map(int,input().split()))
maxx=l[0]
for i in range(n):#using index location
    if l[i]>maxx:
        maxx=l[i]
l.remove(maxx)
maxx=l[0]
for i in l:#calling list value directly
    if i>maxx:
        maxx=i
print(maxx)
