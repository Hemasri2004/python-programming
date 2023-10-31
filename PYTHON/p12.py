sno=int(input("Enter no:"))
sname=input("Enter name:")
grp=input("Enter group:")
s1=int(input("Enter s1 marks"))
s2=int(input("Enter s2 marks"))
s3=int(input("Enter s3 marks"))
total=s1+s2+s3
avg=total/3
print("Total:",total)
print("Average:",avg)
if avg>=90:
 print("O Grade")
elif avg>=80:
 print("A Grade")
elif avg>=70:
 print("B Grade")
elif avg>=60:
 print("c Grade")
elif avg>=50:
 print("D Grade")
else: 
 print("Pass")