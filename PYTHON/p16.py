sh=500
sa=450
ds=600
print("--------WELCOME TO HS SHOPPING MALL--------")
cname=input("Enter customer name:")
cphno=input("Enter phone number:")
shq=int(input("Enter no of shirts:"))
saq=int(input("Enter no of sarees:"))
dsq=int(input("Enter no of dresses:"))
bill=(sh*shq)+(sa*saq)+(ds*dsq)
if bill>=2500:
 disc=bill*15/100
elif bill>=1800:
 disc=bill*9/100
elif bill>=1200:
 disc=bill*5/100
else:
 disc=bill*2/100
tbill=bill-disc
gst=tbill*10/100
obill=tbill+gst
print("Customer name:",cname)
print("Customer phno:",cphno)
print("Shirts:",shq,"*",sh,"=",shq*sh)
print("Sarees:",saq,"*",sa,"=",saq*sa)
print("Dresses:",dsq,"*",ds,"=",dsq*ds)
print("Total",bill)
print("Discount",disc)
print("GST 10%:",gst)
print("Total amount :",obill)
print("<<<<<<<<<Thank you!!!>>>>>>>>>")