fruits=['banana','mongo','apple']

for i in fruits:
    if 'a' in i:
        print(i)
# GIVEN ANS.
b=[]
for j in fruits:
    if j in 'a':
        b.append(j)
        print(b)


a=[x for x in fruits if 'a' in x]
print(a)

s="Praveen"
print(s[::-1])

def checkPalindromwe():
    s1=input("Enter String")
    if s1==s1[::-1]:
        print('String is Palindrome')
    else:
        print('String is not Palindrome')

checkPalindromwe()

'''
Difference between List,tuple & Dictionary:
---------------------------------------------
    List and tuple is an ordered collection of items. 
    Dictionary is unordered collection. 
    List and dictionary objects are mutable 
    i.e. it is possible to add new item or delete and item from it. 
    Tuple is an immutable object
'''