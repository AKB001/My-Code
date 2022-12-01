from tkinter import *
def main():
    a=int(input("Enter the Numbe"))
    print(reverse(a))
def reverse(x):
    rev=0
    temp=x
    while temp!=0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    resLabel=(text="The reverse of a given no is "+str(rev))

    return rev
def createwidgets():
    head= Label(text="Reverse of a number",fg='dark orange',font='arial')
    head.grid(row=0,column=0,columnspan=4)
    Label(text="Enter a number").grid(row=0,column=0)
    a=Text(width=30,height=1)
    aVar=a.get("1.0","end-1c")
    a.grid(row=1,column=1)
    Button("Reverse",command=lambda:reverse(int(aVar))).grid(row=2,column=1,columnspan=4)
def gui():
    root=Tk()
    root.geometry('400x100')
    createwidgets()
    root.mainloop()
#main
gui()




