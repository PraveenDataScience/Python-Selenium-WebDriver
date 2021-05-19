l=[1,5,4,8,9,6,5,4,4]

x=(set([a for a in l if l.count(a)>1]))
print(x)