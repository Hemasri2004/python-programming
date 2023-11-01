n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
print(max(l))
print(min(l))
print(max(l)-min(l))
