'''
    To open the file, use the built-in open() function.
    Mode	Description
    'r'	        Open for text file for reading text
    'w'	        Open a text file for writing text
    'a'	        Open a text file for appending text
2) Reading text methods
The file object provides you with three methods for reading text from a text file:

read() – read all text from a file into a string.
        This method is useful if you have a small file and you want to manipulate the whole text of that file.

readline() – read the text file line by line and return all the lines as strings.
readlines() – read all the lines of the text file and return them as a list of strings.

3) close() method
The file that you open will remain open until you close it using the close() method.
'''
f=open("D:\\New folder\\test1.txt","r")
#print(f.read())
#print(f.readline())
print(f.readlines())
