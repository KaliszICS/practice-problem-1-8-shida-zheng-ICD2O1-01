'''
    Lesson: Boolean Logic
    Author: Mr. Kalisz
    Date Created: Sept 26, 2024
    Date Last Modified: Sept 26, 2024
'''

#Creating booleans - Comparisons

bool1 = 5 > 3
print(bool1)#True

#AND

print(True and False) #False

#OR

print(True or False) #True

#NOT

print(not False) #True

#Syntax

num = 3

#Positive and less than 5

#DONT DO THIS - 0 < num < 5

print(num > 0 and num < 5)
#True and True
#True
#Comparison need to be done 1 at a time

print(False and False or True)  #True
#False or True
#True

print(True or False and False) #True
#True or False
#True

print(not True and False or not True and False)
#False and False or False and False
#False

print(True or not False and not True and False or not True and False or True)
#True

#If it starts with "True or", or ends with "or True", the rest of the line is irrelevant

print(not(not(not(not(True))))) #True
#pairs of nots cancel each other out

#DO NOT DO THIS

word = "Bye"

print(word == "Computer" or "Hello")
#False or "Hello"

print(word == "Computer" and "Hello")