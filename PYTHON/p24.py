num=int(input())
temp=num
sum=0
while(num>0):
    dig=num%10
    sum=sum+dig*dig*dig
    num=num//10
if(temp==sum):
    print("Armstrong!")
else:
    print("Not a Armstrong")