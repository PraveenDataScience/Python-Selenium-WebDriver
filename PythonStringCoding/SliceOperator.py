s = "VDS TECH LABS"
print(s[::-1])


def reverseString():
    rev = input("Enter the String: ")
    output = rev[::-1]
    print(output)


# reverseString()

# Using reversed method:

s2 = "Fiserv"
r = reversed(s2)
output=''.join(r)
print(output)
