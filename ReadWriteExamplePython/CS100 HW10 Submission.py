"""
Joseph Choi
Professor Leon Vaks & Daniel Engelberth
10/31/2015
Homework 10 Submission
"""

#Problem 4.27 from textbook
"""Initialize readfile and writefile"""
readfile = open("readthis.txt", "r")
readfile.close()
writefile = open("writehere.txt", "r")
writefile.close()


def fcopy(readFromFile,writeToFile):
    #open read file and store text inside variable named text
    readF = open(readFromFile, "r")
    text = readF.read()
    readF.close()
    #open write file and write value of variable text inside
    writeF = open(writeToFile, "w")

    for line in text:
        writeF.write(line)
    writeF.close()
    
    
fcopy("readthis.txt", "writehere.txt")


#Problem 4.29 from textbook

def stats(fileToReadFrom):
    #word count
    readF = open(fileToReadFrom, "r")
    words = readF.read()
    readF.close()

    wordCount = words.split()

    #line count    
    readF = open(fileToReadFrom, "r")
    lines = readF.readlines()
    readF.close()

    #char count
    readF = open(fileToReadFrom, "r")
    chars = readF.read()
    readF.close()
    counter = 0
    for line in wordCount:
        counter += len(line)

        
    

    
    
    #line count
    print(len(lines))
    #word count
    print(len(wordCount))
    #characters count
    print(counter)
    

stats("example.txt")

#Problem 3 from text document
def repeatWords(infile,outfile):
    read = open(infile, "r")
    temp = read.readlines()
    read.close()

    d = {}
    d["repeatW1"] = "sit", "Sit"
    d["repeatW2"] = "too"
    

    for words in temp:
        if(words == d["repeatW1"]):
            print(words)

    
    print(temp)
repeatWords("prob3.txt","prob3out.txt")
    
        
