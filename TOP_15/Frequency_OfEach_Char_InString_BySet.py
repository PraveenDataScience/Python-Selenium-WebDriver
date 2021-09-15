s=input("Enter String: ")

s1=set(s)

for ch in sorted(s1):
    print('{} count {} times'.format(ch,s.count(ch)))
