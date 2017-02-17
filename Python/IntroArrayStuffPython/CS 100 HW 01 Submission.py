#Joseph Choi
#CS100 2015F 
#HW 00, September 12, 2015

#Exercise 2.18
print("Exercise 2.18")

#a
print("Part a")
flowers = ["rose","bougainvillea", "yucca","marigold","daylilly","lilly of the valley"]
#Testing Print to see values entered correctly
print(flowers)
print("\n")

#b
print("Part b")
print('potato' in flowers)
print("\n")

#c
print("Part c")
thorny = [flowers[0],flowers[1],flowers[2]]
print(thorny)
print("\n")

#d
print("Part d")
poisonous = [flowers[-1]]
print(poisonous)
print("\n")

#e
print("Part e")
dangerous = [thorny, poisonous]
print(dangerous)
print("\n")

#Exercise 2.19
print("\n\nExercise 2.19")

x = [0,1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]
y = [0,1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9]

#a
print("Part a")
print(0 in x and 0 in y)
print("\n")

#b
print("Part b")
print(10 in x and 10 in y)
print("\n")


#c
print("Part c")
print(6 in x and -6 in y)
print("\n")

#d
print("Part d")
print(-7 in x and 8 in y)
print("\n")


#NOTE! My understanding is that with a radius 10 and starting point 0,0 that this
#circle has the Diameter of 20. So left to right it would be -9 to 0 for one half
#and 0 to 9 for the second half. Unless I was supposed to start from 1-10 this should
#be correct.
print("Please Read Comments in Source Code pertaining to Exercise 2.19!")


#Exercise 2.21
print("\n\nExercise 2.21")

s = ['t','o','n']
#print to test that it is entered correctly
print(s)
#now apply reverse
s.reverse()
print(s)


#Question 3 from HW Word Doc
print("\n\n Question 3 from HW 01 Word Document")
grades = ['A','F','C','F','A','B','A']
#print to see that values entered correctly
print(grades)
#Using count() can always give the proper frequency
frequency = [grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('F')]
print(frequency)
