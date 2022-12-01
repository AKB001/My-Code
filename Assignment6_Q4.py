#Armstrong no
def armstrong():
    num=int(input("Enter any Number :"))
    temp=num
    s=0
    c=0
    while temp!=0:
        c=c+1
        temp=int(temp/10)
    temp=num
    while temp!=0:
        rem=temp%10
        p=1
        for i in range(0,c):
            p=p*rem
        s=s+p
        temp=int(temp/10)
    if s==num:
        print("It's an Armstrong No ",num)
    else:
        print("Oh! Sorry It's not a Armstrong  No ",num)
armstrong()
