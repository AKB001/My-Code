#fibonacci series
n=int(input("Enter the number upto which you want to print :"))
a=0
b=1
for i in range(0,n):
    print(a)
    c=a
    a=b
    b=b+c
