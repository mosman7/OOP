
age = int(input("enter age"))
def movie_rating(age):
    if age >= 117:
        print("please input an age below 117")
    elif 18 <= age:
        print("You can watch all movies")
    elif 16<= age <18:
        print("you cannot watch 18 rated movies")
    elif 12<= age < 15:
        print("you cannot watch 16+ movies")
    elif age < 12:
        print("parental guidance required")
    else:
        print("try again")
    return f"your age is {age}"
print(movie_rating(age))
