
def perfect(n):
 sum=0
 for i in range(1,n):
  if n%i==0:
   sum=sum+i
 if n==sum:
   print("PERFECT NUMBER")
 else:
   print("NOT PERFECT NUMBER")
t=int(input())
for i in range(1,t+1):
 n=int(input())
 perfect(n)