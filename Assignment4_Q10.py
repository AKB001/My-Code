#longest word in a sentence
sentence=input("Enter the line to be measured :")
words =sentence.split()
print(words)
largest= len(words[0])
for i in words:
    word_length=len(i)
    if word_length>largest:
        largest=word_length
        current=i
print("Longest word is : ",current)
print("Length is :",largest)


