#joseph choi
#CS100-103 Professor Leon Vaks & Daniel Engelberth
#HW06 Submission 10/3/2015
#Finish the rest of midterm practice exam 1
"""
6.A I actually can not understand why this is the answer despite looking at pythontutor. I need a in person explanation to this one.
7.E because it should only display "Give Exam Car wont Start"
8.D
9.B
10.D I also need this explained
"""
#12 I added extra words to test my logic
eliza = ['the','rain','in','spain','falls','mainly','on','the','plain', 'otto', 'motto', 'talia']
firstLetter = 't'
def beginsWith(letter,strList):
    accumulator = 0
    for word in strList:
        if(letter in word):
            if(letter == word[0]):
                accumulator += 1
    return accumulator

print(beginsWith(firstLetter, eliza))
            
    
        
#13
def greeting(greetStr):
    uName = input("Whats your name buddy?")
    uDay = input("Whats the day of the week pal?")
    if(len(uName) == len(uDay)):
        print(str(greetStr)+' ' + str(uDay)+' ' + str(uName))
        print("Your name has the same number of characters as today!")

greeting('Happy')
