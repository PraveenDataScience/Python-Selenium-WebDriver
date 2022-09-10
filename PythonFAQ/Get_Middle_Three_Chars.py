def getThreeMiddleChars():
    s=input("Enter string: ")
    l=len(s)
    m=int(l/2)
    string=s[m-1:m+2]
    print("Middle three chars : ",string)


getThreeMiddleChars()