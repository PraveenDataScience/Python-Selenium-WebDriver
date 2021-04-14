def countX(lst,x):
    count=0
    for ele in lst:
        if ele==x:
            count=count+1
    return count

li=[4,5,8,4,5,2,1,4]
print(countX(li,4))

def countN(lst,x):
    return lst.count(x)

print(countN(li,5))