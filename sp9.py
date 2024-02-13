'''write a program to generate salary bill for employee
emno,empname,designation,basic,hra,da,ta
print empno,empname,designation,basic,hra,da,ta,netsalary,tax
where netsalary=basic+da+ta+hra
where tax is depending on net salary
if netsalary>50,000->tax is 5%
if netsalary>35000->tax is 3%
it netsalary>20000->tax is 1%
otherwise tax=0

'''


class Employee:
    def getdata(self,emno,emname,emdgn,embsc,emhra,emda,emta):
        self.emno=emno
        self.emname=emname
        self.emdgn=emdgn
        self.embsc=embsc
        self.emhra=emhra
        self.emda=emda
        self.emta=emta
    def putdata(self):
        print('Employee no:',self.emno)
        print('Employee name:',self.emname)
        print('Employee designation:',emdgn)
        print('Employee basic:',self.embsc)
        print('Employee HRA:',self.emhra)
        print('Employee DA:',self.emda)
        print('Employee TA:',self.emta)
        sal=embsc+emhra+emda+emta
        print('Employee Net Salary:',sal)
        if sal>50000:
            tax=(sal*5)//100
        elif sal>35000:
            tax=(sal*3)//100
        elif sal>20000:
            tax=(sal*1)//100
        else:
            tax=0
        print("TAX:",tax)
        


eb=Employee()
emno=int(input("Enter employee number:"))
emname=input("Enter employee name:")
emdgn=input("Enter employee designation:")
embsc=int(input("Enter employee basic:"))
emhra=int(input("Enter employee HRA:"))
emda=int(input("Enter employee DA:"))
emta=int(input("Enter employee TA:"))
eb.getdata(emno,emname,emdgn,embsc,emhra,emda,emta)
eb.putdata()
