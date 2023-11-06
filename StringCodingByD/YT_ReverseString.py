def reverseByForLoop():
    s = input("Enter String: ")
    rev = ""
    for i in s:
        rev = i + rev
    return rev


# op=reverseByForLoop()
# print(op)

def reverseBySlice():
    s1 = input("Enter String: ")
    op = s1[::-1]
    print(op)


reverseBySlice()
