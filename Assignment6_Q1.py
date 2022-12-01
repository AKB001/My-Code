#prime no or not
def prime():
    count=0
    n=int(input("Enter the number to be checked : "))
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if(count==2):
        print("It's a prime Number ")
    else:
        print("It's Not a prime No ")
prime()