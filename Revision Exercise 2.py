#Adam Howe
#Revision Exercise 2
#02/12/2014

import pdb

def validate(number):
    if number % 2 == 0:
        print("That number is not odd, the program will not work...")
    else:
        print("Number is odd")
        print()

def pyramid(number,space):
    space_number = 1
    while number >= 1:
        print(number * "*")
        number = number - 2
        print("{0}".format(space * space_number),end="")
        space_number = space_number + 1
     
     
space = " "

##pdb.set_trace() 

number = int(input("Enter an odd number: "))
print()

validate = validate(number)

pyramid = pyramid(number,space)


