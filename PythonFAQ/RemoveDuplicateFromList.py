li = [1, 2, 4, 5, 2, 1, 4]


# 1


bl = []
for i in li:
    if i not in bl:
        bl.append(i)



print(bl)

#print(findDulplicate(li))

# 2
print(set(li))
