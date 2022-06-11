a=[1,2,3]
b=a.append(4)
print(a)
print(b)
#====================
l1=[1,2,3]
l2=[4,5,6]
print([x*y for x in l1 for y in l2])
#=============================
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)