#odd number from a list
numbers = input('list: ')
# Convert, for example: "1, 3, 5" -> ["1", " 3", " 5"]
number = numbers.split(",")

total = 0

for a in number:
    # Since these numbers are strings, they need to be converted to
    # integers. You may also want to strip whitespace
    if int(a.strip()) % 2 == 1:
        total = total + 1

print("odd number : ", total)