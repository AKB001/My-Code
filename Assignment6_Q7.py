#Input a list and reverse a string
def list():
    n=int(input("Lenght of list"))
    list1=[]
    for i in range(n):
        element=int(input("Enter the elements:"))
        list1.append(element)
    list2=''.join(map(str,list1))
    list3=list2[: : -1]
    print("List elements are \t:",list3)
list()
