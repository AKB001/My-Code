##Write a program that accepts user input as a string and counts how many times ‘a’ got repeated
test_str = input(str("Enter the word :"))
count = 0
for i in test_str:
    if i == 'a':
        count = count + 1
print ("Count of a in word is : "+str(count))
