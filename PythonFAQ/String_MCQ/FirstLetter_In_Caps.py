# I/P: 'first_name middle_name last_name'
# O/P: 'First_Name Middle_Name Last_Name'

s1=input("Enter string: ")
o=[]
tmp1=s1.split(" ")
for i in tmp1:
    j=i.split("_")
    k="_".join(k.capitalize() for k in j)
    o.append(k)

print("After : ", " ".join(o))