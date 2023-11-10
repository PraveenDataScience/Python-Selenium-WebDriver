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
