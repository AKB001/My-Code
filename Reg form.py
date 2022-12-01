from tkinter import *
root=Tk()
root.geometry("500x500")
def getvals():
    print("Accepted")
Label(root,text="Welcome to CDAC Registration form",font="ar 15 bold").grid(row=0,column=3)
Name=Label(root,text="Name")
Phone=Label(root,text="Phone")
Email=Label(root,text="Email")
State=Label(root,text="State")
Payment=Label(root,text="Payment")
Name.grid(row=1,column=2)
Phone.grid(row=2,column=2)
Email.grid(row=3,column=2)
State.grid(row=4,column=2)
Payment.grid(row=5,column=2)
Namevalue=StringVar
Phonevalue=StringVar
Emailvalue=StringVar
Statevalue=StringVar
Paymentvalue=StringVar
checkvalue=IntVar
Nameentry=Entry(root,textvariable=Namevalue)
Phoneentry=Entry(root,textvariable=Phonevalue)
Emailentry=Entry(root,textvariable=Emailvalue)
Stateentry=Entry(root,textvariable=Statevalue)
Paymententry=Entry(root,textvariable=Paymentvalue)
Nameentry.grid(row=1,column=3)
Phoneentry.grid(row=2,column=3)
Emailentry.grid(row=3,column=3)
Stateentry.grid(row=4,column=3)
Paymententry.grid(row=5,column=3)

Button(text="Submit",command=getvals).grid(row=8,column=3)



root.mainloop()
