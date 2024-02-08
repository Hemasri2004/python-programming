s={}
n=int(input("Enter number of Students:"))
for i in range(n):
    l=[]
    htno=int(input("Enter hallticket number:"))
    sname=input("Enter student name:")
    s1=int(input("Enter sub1 marks:"))
    s2=int(input("Enter sub2 marks:"))
    s3=int(input("Enter sub3 marks:"))
    s4=int(input("Enter sub4 marks:"))
    s5=int(input("Enter sub5 marks:"))
    l.append(sname)
    l.append(s1)
    l.append(s2)
    l.append(s3)
    l.append(s4)
    l.append(s5)
    s[htno]=l
hno=int(input("Enter hallticket number:"))
print("Name of the Student",s[hno][0])
total=s[hno][1]+s[hno][2]+s[hno][3]+s[hno][4]+s[hno][5]
avg=total//5
print("Total:",total)
print("percentage:",avg)
if avg>60:
        print("PASS")
else:
    print("FAIL")
    
    
