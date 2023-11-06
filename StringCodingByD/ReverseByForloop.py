def revByFor():
    s = input("Enter String: ")
    rev = ""
    for i in s:
        rev = i + rev
    return rev


print(revByFor())
