def byWhileLoop():
    s = input("Enter the String: ")
    op = ""
    i = len(s) - 1
    while i >= 0:
        op = op + s[i]
        i = i - 1
    print(op)


# byWhileLoop()

def byRev():
    s = input("Enter the String: ")
    r = reversed(s)
    x = ''.join(r)
    print(x)


# byRev()

def byRecu(s):
    if len(s) == 0:
        return s
    else:
        return byRecu(s[1:]) + s[0]


op = byRecu("VDS TECH")
print(op)
