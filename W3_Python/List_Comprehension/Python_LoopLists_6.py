# Loop through a list:
l1 = ["apple", "banana", "orange"]

for x in l1:
    print(x)

print("=====>Loop Through the Index Numbers")
# Loop Through the Index Numbers
# Use the range() and len() functions to create a suitable iterable.

l2 = ["Ram", "Shyam", "Krishna", "Durga"]

for i in range(len(l2)):
    print(l2[i])


print("======>Using a While Loop")
# Using a While Loop
l3=["Python","Java","C#","Ruby"]
i=0
while i<len(l3):
    print(l3[i])
    i=i+1

print("======> Looping Using List Comprehension")
# Looping Using List Comprehension
l4 = [10,11,12,13,14,15,16,17,18]
num = [x for x in l4 if x%2==0]
print(num)