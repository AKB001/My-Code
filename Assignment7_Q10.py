num = [int(input("Enter a number: "))]
table = list(map(lambda x, y: x * y, list(range(1, 11)), num * 10))
print(table)