#product of number
# Take input from user
num = int(input("Enter any number : "))

a = num
Multiply = 1;

while(a != 0):

    Multiply = Multiply * (a % 10);

    # Remove last digit from temp.
    a= int(a / 10)

print("\nProduct of all digits in", num, ":", Multiply)