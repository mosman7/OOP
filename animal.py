# create a class called animal - file name starts with a - class name starts with A
# add the common attributes/ var behaviour/ functions
# syntax class name: - class Animal
class Animal: # follow the
    #first we initialise the class using builtin method called __init__(self)
    #self refers to current class
    def __init__(self): # any attributes attached to the class should be part of the init method
        # self.var = True
        self.alive = True
        self.spine = True
        self.eyes = True

# create some methods to add common behaviours
    def breathe(self):
        return "keep breathing to stay alive"
    #add 1 more behaviour
    def eat(self):
        return "Its lunch time"

# create an object of the class - must have an object to use the methods
cat = Animal() #creating an object of our Animal class
# print(cat.breathe()) #calling the method
# print(cat.eat())