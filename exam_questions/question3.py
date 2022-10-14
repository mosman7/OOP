word = input("Enter password")
def pass_length(word):
    if len(word) < 5:
        print("too short")
    elif len(word) > 20:
        print("too long")
    elif 5 < len(word) < 20:
        print("acceptable")

pass_length(word)