def palindrome(val):
    x=val[::-1]
    if x==val:
        print("This is Palindrome")
    else:
        print("This is not a palindrome")


palindrome('MADAMA')