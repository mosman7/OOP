from reptile import Reptile
class snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue(selfs):
        return "I will eat you"

smart_snakes = snake()
print(f"this function is called from the current class{smart_snakes.use_tongue()}")
print(smart_snakes.hunt())
print(smart_snakes.breathe())
