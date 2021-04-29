vowels=['a','e','i','o','u']

word=input("Enter the word to search for vowels: ")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(found)
print("The number of different vowels present in",word, 'is',len(found))


