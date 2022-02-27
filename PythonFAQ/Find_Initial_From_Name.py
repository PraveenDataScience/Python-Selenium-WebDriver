def printInitials(name):
    if (len(name) == 0):
        return

    # Split the string using 'space'
    # and print the first character of
    # every word
    words = name.split(" ")
    for word in words:
        print(word[0].upper(), end=" ")


# Driver code
if __name__ == '__main__':
    name = "Praveen Kumar Mishra"
    printInitials(name)