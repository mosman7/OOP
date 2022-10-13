# lucky draw
# import - imports from external libraries folder on the left
# import random      # allows us to generate something random
# print(random.random()) # prints a random number each time - calls the random folder
#
# from random import *       # from this flder import this
# print(random())


# import math
# import datetime, sys
# import os
# print(os.cpu_count())
# print(datetime.date.today())
# print(datetime.time



#
# number = 23.9
# #round numbers .5 and above up
# #numbers.49 and below round down
# print(math.ceil(number))        # ceil rounds everything up
# print(math.floor(number))       # floor rounds everything down

# def greeting ():            # defines a function called greeting
#    print("hello")
# greeting()                    #can only print after function is called
#   #  pass

#greet a user with name
# def greet_user(name):               # create a fu7nction that takes an argument -argument is name
#     print("Hello", name)            # adding 2 strings, calling name function
#     #pass
# greet_user("Mohamed")

def add(v1, v2):                    #creates function add, takees 2 values
    print("your result is", v1 + v2) #tells the function what to do
add(3, 7)

def add(v1, v2):                    #creates function add, takees 2 values
    print("your result is", v1 + v2) #tells the function what to do
    return v2 + v1                  # if you are using a return statement and calling the function it needs to be in a print as below

print(add(2, 7))                           #adds the 2 values



# create a function to *
def mul(x1, x2)
    print("your values multiplied is", x1 * x2)
mul(3, 6)
# create a function to %
# create a function to /
# research return statement and use it instead of print in your functions
# optionals
# create a function to convert CM to M - inches to CM - meter into feet
