list1=["apple","banana","cherry",10,20,33]
print(len(list1))

list1[-1]="Deepak"
print(list1)

list1[:4]=["Ram",55,"Krishna",50]
print(list1)

list1[3:5]=["watermelon","papya"]
print(list1)

list1[3:5]=["watermelon","papya","Reep"]
print(list1)

list1[3:5]=["watermelon","papya","Reep","seep"]
print(list1)

print("===============")

list1[1:4]=["Rampa"]
print(list1)

# INSERT METHOD:

list2 = [11,44,22,33]
list2.insert(2,"Ram")
print(list2)