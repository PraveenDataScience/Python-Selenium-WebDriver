# Without Comprehension:
l1=["apple","banana","orange","cherry","kiwi","mango"]
nl=[]

for x in l1:
    if "a" in x:
        nl.append(x)

print(nl)

# By using Comprehension:
l2=["apple","banana","orange","cherry","kiwi","mango"]

new=[x for x in l2 if "n" in x]
print(new)

# Only accept item that are not apple:

new1=[x for x in l2 if x!="apple"]
print(new1)

# Iterable:

l3 = [x for x in range(10) if x<6]
print(l3)

# Expression:

l4=[x.upper() for x in l2 ]
print(l4)

l5 = [ x if x!="banana" else "ratna" for x in l2]
print(l5)