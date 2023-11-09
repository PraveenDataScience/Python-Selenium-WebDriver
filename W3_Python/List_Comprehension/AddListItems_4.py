# Append item:
list1 = ["apple", "banana", "cherry", "orange"]
print(list1)

# Insert Item at specified position:

list1.insert(3,"papaya")
print(list1)

# Extend List:
l1=[1,4,8,9]
l2=["Ram","Shaym"]

l1.extend(l2)
print(l1)

# Add any Iterable by using extend() method:

l3=["apple","banana","cherry"]
l4=("kiwi",55)

l3.extend(l4)
print(l3)