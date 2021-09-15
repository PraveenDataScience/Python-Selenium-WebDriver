lst=[1,5,4,2,3,6,9,6,3,6,5,2,1,4]
print("Input List: ",lst)

lst1=[]
count=0

# Traverse the array:
for i in lst:
    if i not in lst1:
        count=count+1
        lst1.append(i)

print("Output List: ",lst1)
print("No. of unique items are: ",count)