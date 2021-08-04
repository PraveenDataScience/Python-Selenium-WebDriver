def rev(s):
    if len(s)==0:
        return s
    else:
        return rev(s[1:])+s[0]

s1="This is VDS Tech Labs"
print(rev(s1))