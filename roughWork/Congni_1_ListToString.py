# Covert List to String:
#1 Way:
def lisstToStrig(s):
    str1=''
    for ele in s:
        str1+= ele
    return str1

l1=['job','bob','merry']
print(lisstToStrig(l1))

#2nd way:
s1=" ".join(l1)
print(s1)

# 3rd way: Using LC
s2 = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
str2= " ".join([str(ele) for ele in s2])
print(str2)