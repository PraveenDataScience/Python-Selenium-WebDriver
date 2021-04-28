li=[4,5,6,8,9,5,6]

print("==========Simple for loop==========================")
for x in li:
    print(x)

print("==============for loop using range ======================")
length=len(li)
for a in range(length):
    print(li[a])

print("============== Iterate using while loop ======================")

i=0
while i<length:
    print(li[i])
    i=i+1

print("============== Using List Compherension ======================")
print("==ODD===")
l1=[4,7,8,5,2,3,6,9]
[print(x) for x in l1 if x%2!=0]
print("==EVEN===")
[print(x) for x in l1 if x%2==0]