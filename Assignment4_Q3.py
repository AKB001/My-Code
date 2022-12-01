#sum of even and odd number
nums = []
sumeven = 0
counteven = 0
sumodd = 0
countodd = 0

print("Enter the size of list: ", end="")
tot = int(input())
print("Enter", tot, "Elements for the list: ", end="")
for i in range(tot):
    nums.append(int(input()))
    if nums[i]%2 == 0:
        sumeven = sumeven + nums[i]
        counteven = counteven + 1
    else:
        sumodd = sumodd + nums[i]
        countodd = countodd + 1

if counteven==0:
    print("\nEven number is not found in this list!")
else:
    print("\nSum of Even Numbers =", sumeven)
if countodd==0:
    print("Odd number is not found in this list!")
else:
    print("Sum of Odd Numbers =", sumodd)