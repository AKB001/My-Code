#reverse a word in a sentence 
str1=input("Enter the sentnece :")
words = str1.split()
rev_str1=[]
for i in words:

    rev_str1.append(i[::-1])
final=" ".join(rev_str1)
print(final)
