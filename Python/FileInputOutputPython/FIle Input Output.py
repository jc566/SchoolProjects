inFile = open("Holla.txt", "r") #open/create text file
print(inFile.read())            #read the entire file

#R to nullfiy backslash which are escapes

aList = ["open", "it", "up"]
emptyfile = open("TestFile.txt", "w")
for line in aList:              #traverse through and write
    emptyfile.write(line + '\n')
emptyfile.close()               #must close file to actually have write completed

emptyfile = open("TestFile.txt", "r") #open file
print(emptyfile.read())               #read file
emptyfile.close()                     #close file




humptyfile = open("humpty.txt", "r")
for line in humptyfile:
    if 'humpty' in line:
        
        print(line,sep = ' ')
humptyfile.close()

print("\n\n\n")

#consecutive reading
#almost like bookmarks
print("consecutive reading")
humptyfile = open("humpty.txt", "r")
print(humptyfile.read(7))
print(humptyfile.read(3))
#print(humptyfile.read(27))
humptyfile.close()

print("\n\n\n")

#cursors -> pointers of bookmarks
print("cursors -> pointers of bookmarks")
humptyfile = open("humpty.txt", "r")
print(humptyfile.readline())
print(humptyfile.readline())
print(humptyfile.readline())
humptyfile.close()

print("\n\n\n")

#readlines, allows you to read multiple lines
#creates a list
print("readlines, allows you to read multiple lines, creates list")
humptyfile = open("humpty.txt", "r")
print(humptyfile.readlines())
humptyfile.close()

print("\n\n\n")

#function - reading the words inside text file
#then it returns the number of words inside
print("function - reading the words inside text file then it returns the number of words inside")
def numWords(filename):
    inFile = open(filename, 'r')
    text = inFile.read()
    inFile.close()
    txtlist = text.split()
    return len(txtlist)

print(numWords("humpty.txt"))

print("\n\n\n")



