
def armstrong(n):
    sum=0
    temp=n
    while n!=0:
        rem=n%10
        sum=sum+rem*rem*rem
        n=n//10
    if sum==temp:
        return True
    else:
        return False
n=int(input())
l=[i for i in range(1,n+1) if armstrong(i)]
for i in l:
    print(i,end=" ")
