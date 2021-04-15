import numpy as np
# list=[expression for item in Iterable (if condition)]
# Using LC
a=[4,6,7,8,2,3,5]
li1=[x for x in a if x>=5]
#print(li)
# The equivalent for loop is:
l1=[]
for i in li1:
    if i>5:
        l1.append(i)
#print(li1)

b = []
for x in li1:
  if x > 5:
    b.append(x)
'''
We can also do something with items before putting them in a new list:
We multiply the items that fit the condition by 2 and then put in a list.
'''
a1 = [4,6,7,3,2]
li2=[x*2 for x in a1 if x>5]
print(li2)

'''
The condition is that string starts with the letter “c”. 
Since we have both capital and lowercase letters, 
we convert all letters to lowercase first.
'''
names = ['Ch','Dh','Eh','cb','Tb','Td']
li3=[name for name in names if name.lower().startswith('c')]
print(li3)
'''
we can iterate over a 2-dimensional NumPy array which is actually a matrix.
We iterate over the rows in matrix A and take the maximum number.
'''
A=np.random.randint(10,size=(4,4))
print(A)
max_ele=[max(i) for i in A]
print(max_ele)

'''
We iterate over the rows in matrix A and take the maximum number.
Lists can store any data type. Let’s do an example with a list of lists.
'''
vals = [[1,2,3],[4,5,2],[3,2,6]]
max_val=[max(i) for i in vals ]
print(max_val)

print(sum([i for i in range(1, int(input("Enter n: "))+1)]))
''''

'''
