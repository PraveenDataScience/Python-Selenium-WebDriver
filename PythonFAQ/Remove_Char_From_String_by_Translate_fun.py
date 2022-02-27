def remove_char(s1,s2):
    dict={ord(s2):None}
    print(s1.translate(dict))

s1=input("EnterString: ")
s2=input("Enter character: ")
remove_char(s1,s2)