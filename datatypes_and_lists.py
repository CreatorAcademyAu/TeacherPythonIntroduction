#Datatypes and Lists

whole_number = 5 #this is an integer (int)

word = 'word!' #this is a string (str)

decimal = 2.3 #this is a float (float)

print(whole_number/2)
print(type(decimal)) #the type method is used for finding out the datatype

#implicit casting

x = 1
y = 3.5
z = 'hello'

#implicit casting is indirectly telling the computer to use a datatype

print(type(x))

x/=2 #this equals x = x/2

print(type(x))

#explicit casting

m = int(1) #explicitly casting 1 as an int
n = float(1) #explicitly casting 1 as a float
o = str(1) #explicitly casting 1 as a string

#collections

my_fave_foods = ['lasagna','spaghetti','cheese','pizza'] #this is a list

my_fave_numbers = [72,14,89] #this is another list

print(type(my_fave_foods))

library_students = ['Jonno','Macca','Bruce']

print(library_students)

library_students.sort()

print(library_students)

library_students.reverse()

print(library_students)

#a whole bunch of activities can be done by challenging students to write lists

#what if I want to access an item in a list?

print(library_students[0]) #in python, lists are zero based, so 0 is first

#[1] is second etc

print(library_students[-1])#this is the last item in a list

#to find the length of a list
print(len(library_students)) #this finds the length of a list

#let's create a program to say 'good morning' to each student in the library
#cave man/ brute force programming- not good:
"""
print('Good morning',library_students[0])
print('Good morning',library_students[1])
print('Good morning',library_students[2])
"""

#to iterate through a list, we can use a for loop coupled with list methods
for student in range(0,len(library_students),1):
    print('Good afernoon',library_students[student])


#let's create a McDonald's menu

menu = ['Chicken Burger','Hamburger','Milkshake']

for item in range(0,len(menu),1):
    print('Mc'+menu[item])








