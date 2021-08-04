def revByLoop(s):
    rev=""
    for i in s:
        rev=i+rev
    return rev
    print(rev)

print(revByLoop("This is VDS"))