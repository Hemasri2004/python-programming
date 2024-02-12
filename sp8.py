class Number:
    def armstrong(self,n):
        m=n
        sm=0
        while(n>0):
            rem=n%10
            sm=sm+rem*rem*rem
            n=n//10
        if m==sm:
            return True
        else:
            return False
n=int(input())
arm=Number()
if arm.armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")
