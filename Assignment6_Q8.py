#input a tuple and reverse a string
def tuple():
    a=input("Enter some values:")
    a=tuple(int(x) for x in a.split(","))
    b=''.join(map(str,a))
    c=b[: : -1]
    print(c)
tuple()