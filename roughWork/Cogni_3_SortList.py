l1=['Ram','Shyam','VDS','TECH','LABS']
l1.sort()
print(l1)

def sortlen(e):
    return len(e)

l1.sort(key=sortlen,reverse=True)
print(l1)