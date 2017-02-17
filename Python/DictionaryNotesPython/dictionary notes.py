"""
Dictionaries
"""

"""
What data types exist?
Strings
Floats
Integers
Doubles
Characters
Boolean
List - encased in brackets [ ]
Tuple - ( ) encased in parenthesis
dict aka Dictionary - encased in { }
"""
#Dictionary is key:value

"""
2 items in dictionary definition
"""
#create empty dictionary
print("create empty dictionary")
d = {}
print(d)

#one way to populate key and value
print("one way to populate key and value")
d["dogs"] = 3
print(d)

d["cats"] = 2
print(d)

#refer to key not value
print("refer to key not value, for example")
print(d["cats"])

#how can you change the value in side key cats?
#key can not be changes because it is immutable, but value can be changed
d["cats"] = 4
print(d["cats"])

#remove a item in a dictionary use .pop
print(d.pop("cats"))

d["cat"] = [1,2]
print(d["cat"])

checkingAccount = {}
checkingAccount[12345] = 56789
checkingAccount[34512] = 89345
print(checkingAccount)

#how to combine two dictionaries

d.update(checkingAccount)
print(d)

d = {3:1}
a = {2:4}
c = {1:6}
b = {4:1}

d.update(b)
d.update(a)
d.update(c)
print(d)


#iterations for Dictionaries
def readLines(filename):
    d = {}
    count = 0
    inFile = open(filename, 'r')
    for line in inFile:
        d[count] = line
        count += 1
        
    return d
print(readLines("humpty.txt"))


#study this 
def frequency(itemList):
      '''Compute the frequency of each item in      itemList. Return the result as a dictionary       in which each distinct item in itemList is a      key and the item's frequency (count) is the       associated value.'''

      counters = {}

      for item in itemList:
          # if the item hasn't been seen before
          if item not in counters:
              # add the item to the dictionary 
              # and set its count to 1
              counters[item] = 1
          # otherwise, increment the count of item
          else:
              counters[item] += 1

      return counters

print(frequency([95,95,96,97,98,92,93,94,100]))


