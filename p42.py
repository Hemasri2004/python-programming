n=int(input())
s1=list(map(int,input().split()))
m=int(input())
s2=list(map(int,input().split()))
minn=s1[0]
for i in s1:
    if minn<i:
        i=minn
print(minn)
   
    
