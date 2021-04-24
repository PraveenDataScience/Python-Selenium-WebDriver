import re

s="12345abchted#$5^7w@#"

a=[x for x in s if re.sub('[\w]+' ,'', x)]
#print(len("".join(a)))

#x = "asdfklsdf#$&^#@!"
#new = re.sub('[\w]+' ,'', s)
#print(len(new))

# Python program to Count Alphabets Digits and Special Characters in a String

string = input("Please Enter your Own String : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if (string[i].isalpha()):
        alphabets = alphabets + 1
    elif (string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1

print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)