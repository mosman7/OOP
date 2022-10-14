#create a class called reptile
#make the animal class a parent class and inherit from it

from animal import Animal       #importing everything from animal class
class Reptile(Animal): #inheriting from animal class
    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chanbers = [3, 4]

    def hunt(self):
        return "find some food"

    def venom(self):
        return "use your venom"

smart_reptile = Reptile()
# print(smart_reptile.breathe())
# print(smart_reptile.hunt())