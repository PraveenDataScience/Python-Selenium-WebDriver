l1=['Ram','VDS','TECH']
l2=[1,2,3]

# 1st way:
res = {}
for key in l1:
    for value in l2:
        res[key] = value
        l2.remove(value)
        break

print(str(res))

#2 LC:
x={l1[i]:l2[i] for i in range(len(l2))}

print(x)

print("Original key list is : " + str(l1))
print("Original value list is : " + str(l2))

# using zip()
# to convert lists to dictionary
res = dict(zip(l1, l2))

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))

age=36
txt="My name is vanya and my "+str(age)
print(txt)