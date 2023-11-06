# Normal way:

fruits = {"apple", "banana", "cherry", "kiwi", "mango"}

newlist = []
for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

# By List Comprehension:

num = {10,5,8,9,6,20,11,14,12}

nList={x for x in num if x%2==0}
print(nList)


