def rev_palindrome():
    s=input("Enter the String: ")
    if s==s[::-1]:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

rev_palindrome()