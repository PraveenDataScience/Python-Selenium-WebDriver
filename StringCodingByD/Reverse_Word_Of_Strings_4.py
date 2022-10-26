s=input("Enter string to be reversed : ")
l=s.split()
print(l)
l1=l[::-1]
print(l1)
output=' '.join(l1)
print("Reversed String is : ",output)