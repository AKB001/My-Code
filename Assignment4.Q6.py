# various func
#index function
list2 = ['cat', 'bat', 'mat', 'cat', 'pet']
 # Will print the index of 'bat' in list2
print(list2.index('bat'))

#append function
my_list = ['geeks', 'for']
my_list.append('geeks')
print (my_list)

#insert function
vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')
print('List:', vowel)

#extend function
prime_numbers = [2, 3, 5]
numbers = [1, 4]
# add all elements of prime_numbers to numbers
numbers.extend(prime_numbers)
print('List after extend():', numbers)

#sort function
numbers = [1, 3, 4, 2]
# Sorting list of Integers in ascending
numbers.sort()
print(numbers)

#pop function
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
