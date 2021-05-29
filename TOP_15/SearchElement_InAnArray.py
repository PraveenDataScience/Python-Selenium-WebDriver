def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    print("Element is not present")



l=[1,4,7,4,1,5,6,3,2]
print(search(l,1))