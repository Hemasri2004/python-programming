'''
n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
print(l[0])
print(l[-1])

n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
print(max(l))
print(min(l))
print(max(l)-min(l))

4
1 2 3 4 
0 1 2 3

'''
n=int(input())
l=[]
for i in range(n):
    z=int(input())#1 2 8 9
    l.append(z)
x=int(input())#position 1
y=int(input())#new value 2
l[x]=y
print(l)

