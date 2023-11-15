l=[]
n=int(input())
for i in range(0,n):
    x=int(input())
    l.append(x)
maxx=l[0]
for j in range(0,n):
    if(maxx<l[j]):
        maxx=l[j]
print(maxx)
    
