def length(str):
    lis=list(str.split(' '))
    return len(lis[-1])


str="VDS TECH LABS"
print("Length of last word: ",length(str))



y=lambda x : x%2==0

print(y(6))