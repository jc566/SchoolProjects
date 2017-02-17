#Joseph Choi
#CS100 section 103 Professor Leon Vaks & Daniel Engelberth
#9/26/2015

#Problem 3.20 from Perkovic 2nd edition
#Getting a syntax error when trying to name variable 1st. I thought you couldnt
#start a variable name with a number.
print("Output for 3.20")
first = ['January', 'February', 'March']
for month in first:
    print(month)

#Problem 3.21
print("\nOutput for 3.21")
first = [2,3,4,5,6,7,8,9]

for index in range(0,8,2):
    print(first[index])

#Problem 3.22 ***STUDY THIS***
print("\nOutput for 3.22")
first = [2,3,4,5,6,7,8,9]
for i in first:
    if(i**2 % 8 == 0):    
        print(i)

#Problem 3.23
print("\nOutput for 3.23 Part A.")
for i in range(0,2):
    print(i)
print("\nOutput for 3.23 Part B.")
for i in range(0,1):
    print(i)
print("\nOutput for 3.23 Part C.")
for i in range(3,7):
    print(i)
print("\nOutput for 3.23 Part D.")
for i in range(1,2):
    print(i)
print("\nOutput for 3.23 Part E.")
for i in range(0,4,3):
    print(i)
print("\nOutput for 3.23 Part F.")
for i in range(5,22,4):
    print(i)
