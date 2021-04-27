x=1

if x<0:
    raise Exception("number must be +ve")

def strPresent(s):
    if 'vds' not in s:
        raise Exception("The string is not valid")

strPresent("vds tech labs")