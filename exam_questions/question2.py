def is_twin(a,b):
    if sorted(a) == sorted(b):      # sorts words in order
        return True                 # returns true if the same
    else:
        return False
print(is_twin("play", "layp"))