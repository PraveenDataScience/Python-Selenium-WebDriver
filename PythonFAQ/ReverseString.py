# 1.  Using Loops:
def reverse(s):
    rev = " "
    for i in s:
        rev = i + rev
    return rev


# print(reverse("Praveen"))

# 2.  Using recurssion:

def revByRecurrsion(s):
    if len(s) == 0:
        return s
    else:
        return revByRecurrsion(s[1:]) + s[0]


#print(revByRecurrsion("Fiserv"))

# 3. Using extended slice:

def revByExtendedSlice(s):
    s=s[::-1]
    return s

#print(revByExtendedSlice("PYTHON"))

# 4. Using reversed Fun
def revByReversedFun(s):
    s="".join(reversed(s))
    return s

print(revByReversedFun("Priya"))