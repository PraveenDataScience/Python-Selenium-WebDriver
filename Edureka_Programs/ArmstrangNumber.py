num=int(input("Enter the number: "))
s=0
temp = num

while temp > 0:
    c=temp % 10
    s=s+c**3
    temp//=10
if num==s:
    print("It is a Armstrang Number")
else:
    print("It is not a Armstrang Number")