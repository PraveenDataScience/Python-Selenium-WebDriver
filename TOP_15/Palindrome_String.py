def palindrome(s):
    if s[::-1]==s:
        print("Palindromwe")
    else:
        print("Not Palindrome")

s1="NITIN"
palindrome(s1)

# Using in-built reversed() fun:

def isPalindrome(s2):
    rev=''.join(reversed(s2))

    if rev==s2:
        return True
    else:
        return False

print(isPalindrome("Madam"))