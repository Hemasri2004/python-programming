def myresult():
    s1=int(sem1marks.get())
    s2=int(sem2marks.get())
    s3=int(sem3marks.get())
    s4=int(sem4marks.get())
    s5=int(sem5marks.get())
    s6=int(sem6marks.get())
    total=s1+s2+s3+s4+s5+s6
    avg=total//6
    if avg>=10:
        gr='O'
    elif avg>=9:
        gr='A+'
    elif avg>=8:
        gr='A'
    elif avg>=7:
        gr='B'
    elif avg>=6:
        gr='C'
    elif avg>=5:
        gr='D'
    elif avg>=4:
        gr='P'
    else:
        gr='F'
    r='Grade:'+gr
    s.config(text=r)

from tkinter import *
result=Tk()
result.title('Results')
sem1=Label(result,text="Enter sem1 marks")
sem1marks=Entry(result)
sem2=Label(result,text="Enter sem2 marks")
sem2marks=Entry(result)
sem3=Label(result,text="Enter sem3 marks")
sem3marks=Entry(result)
sem4=Label(result,text="Enter sem4 marks")
sem4marks=Entry(result)
sem5=Label(result,text="Enter sem5 marks")
sem5marks=Entry(result)
sem6=Label(result,text="Enter sem6 marks")
sem6marks=Entry(result)
b1=Button(result,text="Submit",command=myresult)
s=Label(result)

sem1.grid(row=0,column=0)
sem1marks.grid(row=0,column=1)
sem2.grid(row=1,column=0)
sem2marks.grid(row=1,column=1)
sem3.grid(row=2,column=0)
sem3marks.grid(row=2,column=1)
sem4.grid(row=3,column=0)
sem4marks.grid(row=3,column=1)
sem5.grid(row=4,column=0)
sem5marks.grid(row=4,column=1)
sem6.grid(row=5,column=0)
sem6marks.grid(row=5,column=1)
b1.grid(row=6,column=0)
s.grid(row=6,column=1)


result.mainloop()
