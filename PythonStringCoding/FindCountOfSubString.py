#1st way:
s="ram amol and amolin aol"
sb='am'
print(s.count(sb))

#2nd way:
def count_substring(string,sub_string):
    count=0
    for i in range(len(string)-len(sub_string)+1):
        if(string[i:i+len(sub_string)] == sub_string ):
            count+=1
    return count

print(count_substring("Ram vds ram vds is good",'vds'))