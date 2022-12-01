import numpy as num

array1 = num.array([0, 10, 20, 40, 60])
print("Array1: ",array1)

array2 =num.array([10, 30, 40])
print("Array2: ",array2)
print("Joining of two arrays is:")
print(num.union1d(array1,array2))
print("Common values are:")
print(num.intersect1d(array1,array2))

