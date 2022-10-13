# lucky draw
# import - imports from external libraries folder on the left
import random      # allows us to generate something random
print(random.random()) # prints a random number each time - calls the random folder

from random import *       # from this flder import this
print(random())


import math
number = 23.9
#round numbers .5 and above up
#numbers.49 and below round down
print(math.ceil(number))        # ceil rounds everything up
print(math.floor(number))       # floor rounds everything down