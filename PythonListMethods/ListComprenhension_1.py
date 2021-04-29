# create list 1-10:
# Simple way:
l=[]
for l1 in range(1,11):
    l.append(l1)

# By Using List Comphrension:
l1=[x for x in range(1,11)]
print(l1)

l2=[x+2 for x in range(1,11) if x%2==0]
print(l2)

l3=[2**x for x in range(1,6)]
print(l3)

#================================
# Print first letter of each string in list:
words=['Vds','Tech','Labs']
l4=[word[0] for word in words]
print(l4)

# Intersection and Union in List
l5=[10,20,30,40]
l6=[30,40,60,70]
#Print common in both l5 & l6:
l7=[x for x in l5 if x in l6]
print(l7)
#Print common in both l5 & l6:
l8=[x for x in l5 if x not in l6]
print(l8)

# make list of Length of words in String with upper case
words="the quick brown fox jumps over the lazy dog"
s=words.split()
print(s)
l9=[[w.upper(),len(w)] for w in s]
print(l9)

