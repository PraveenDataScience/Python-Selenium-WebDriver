s=input("Enter String: ")

l=[]

for i in s:
    if i not in l:
        l.append(i)
for i in sorted(l):
    print('{} count {} times'.format(i, s.count(i)))

