def mysubstract():
    l1=int(l1marks.get())
    l2=int(l2marks.get())
    m=l1-l2
    s="result="+str(m)
    
    res.config(text=s)


from tkinter import *
substract=Tk()
substract.title("Subtraction")
l1=Label(substract,text="Enter 1st number")
l1marks=Entry(substract)
l2=Label(substract,text="Enter 2nd number")
l2marks=Entry(substract)
b1=Button(substract,text="substract",command=mysubstract)
res=Label(substract)



l1.grid(row=0,column=0)
l1marks.grid(row=0,column=1)
l2.grid(row=1,column=0)
l2marks.grid(row=1,column=1)

b1.grid(row=3,column=0)
res.grid(row=3,column=1)


substract.mainloop()
