#palindrome no
def intRev(val):
    inverse = 0
    while(val > 0):
        Remi = val % 10
        inverse = (inverse * 10) + Remi
        val = val // 10
    return inverse

val = int(input("Please Enter any Num: "))
rev = intRev(val)
print("Inverse = %d" %rev)

if(val == rev):
    print("%d is a Palindrome" %val)
else:
    print("%d is not Palindrome" %val)