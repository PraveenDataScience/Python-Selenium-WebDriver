# Create a list which contain square of list element from 1-9

# By using Normal for loop:
ol=[]
for l in range(1,10):
    ol.append(l**2)

print(ol)

# By using List Comprehension:

x=[i*i for i in range(1,11)]
print(x)