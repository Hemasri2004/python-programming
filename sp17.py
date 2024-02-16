n=int(input())
sm=0
m=n
while(n>0):
    rem=n%10
    sm=sm+rem*rem*rem
    n=n//10
if sm==m:
    print("Armstrong")
else:
    print("Not Armstrong")
