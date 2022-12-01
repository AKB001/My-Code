#list to reverse string
# creating an empty list

n=int(input("Lenght of list"))
list1=[]
for i in range(n):
    element=int(input("Enter the elements:"))
    list1.append(element)
list2=''.join(map(str,list1))
list3=list2[: : -1]
print("List elements are :",list3)

