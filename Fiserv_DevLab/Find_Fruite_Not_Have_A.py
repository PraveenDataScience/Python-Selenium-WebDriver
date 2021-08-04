fruits=['apple',"banana","cherry","kiwi","mango"]

# Using For loop:
nl=[]

for i in fruits:
    if 'a' not in i:
        nl.append(i)

print(nl)

# Using List Comphrension:

f2=[a for a in fruits if 'a' not in a]
print(f2)


f=[x for x in fruits if 'a' in x]
print(f)
