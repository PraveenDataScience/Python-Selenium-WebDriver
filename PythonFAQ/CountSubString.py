# Find Sub-String in whole string:


def subStringInWholeString():
    string = input("Enter String: ")
    substring = input("Enter Sub String: ")
    count = string.count(substring)
    # print count
    print("The count is:", count)


#subStringInWholeString()

def subStringByRangeInString():
    string = input("Enter String: ")
    substring = input("Enter Sub String: ")
    count = string.count(substring,5,15)
    # print count
    print("The count is:", count)

subStringByRangeInString()