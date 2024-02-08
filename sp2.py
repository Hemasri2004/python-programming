n=int(input())
c=0
for i in range(2,n):
    if n%i==0:
        c=1
        break
if(c==1):
    print("NOT PRIME")
else:
    print("PRIME")
