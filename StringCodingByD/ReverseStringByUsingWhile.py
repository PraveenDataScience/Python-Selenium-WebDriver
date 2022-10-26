s=input("Enter string to be reversed : ")
output=''
i=len(s)-1
while i>=0:
    output=output+s[i]
    i=i-1
print("Reversed String is : ",output)