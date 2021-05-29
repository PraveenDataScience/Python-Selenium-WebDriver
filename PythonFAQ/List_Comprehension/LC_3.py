#Find the Even number from the list by using normal for loop and by using List Comprehensions
l=[4,5,7,8,9,3,2,10,14,11,15]

# Using for Loop:

ol=[]
for i in l:
    if i%2==0:
        ol.append(i)
print(ol)

# Using LC:
x=[i for i in l if i%2==0]
print(x)

