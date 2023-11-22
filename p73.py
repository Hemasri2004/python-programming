def leap(year):
    if year%400==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False
n,m=map(int,input().split())
l=[i for i in range(n,m+1) if leap(i)]
c=0
for i in l:
    c=c+1
print(c)
