l=[40,5,2,3,6,9,88,74,]
nl=[]

while l:
    min=l[0]
    for x in l:
        if x>min:
            min=x
    nl.append(min)
    l.remove(min)
    #print(nl)

print(nl)
