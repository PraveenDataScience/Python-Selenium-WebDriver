import re
sentence = 'Learn Python Programming'
test = re.match(r'(.*) (.*?) (.*)', sentence)
print(test.group())

num = '5'*'5'
print(num)

#a = [1,2,3,None,(),[],]
#print len(a)

