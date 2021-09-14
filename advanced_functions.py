#Advanced Functions

#a function is normally a tool to 'do' a bunch of things
x = 5
y = 6

def my_add():
    print(x+y)

my_add()

def my_add2(num1,num2): #num1 and num2 are arguments, or parameters
    print(num1+num2)

my_add2(50,6)
my_add2(99,650)

#all the above functions will get python to 'do' something


#function can also get python to 'be' something

#we use a 'return' to make a function transform into a value

def my_add3(num1,num2):
    return num1+num2

print(my_add3(88,15))

#examples

def is_even(my_num):
    if my_num%2==0:
        print(my_num,"is even")
    else:
        print(my_num,"is odd")

is_even(100)


def can_i_drive(age):
    if age>=16:
        print("you can drive")
    else:
        print("you cannot drive")


can_i_drive(16)


def counter(limit):
    for i in range(0,limit,1):
        print(i)

counter(20)





