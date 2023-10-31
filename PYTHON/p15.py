n=int(input("Enter n value:"))
if(n%2==0):
  if(2>=n and n<=5):
   print("Not Weird")
  elif(6>=n or n<=20):
   print("Weird")
  elif(n>20):
   print("Not Weird")
else:
 print("Weird") 