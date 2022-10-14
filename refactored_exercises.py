# Tasks
## Age calc task

def year_born(age):
    this_year = int(2022)
    year_born = this_year - age
    return f"You were born in {year_born}"

age = int(input("Please enter youe age:"))
print(year_born(age))

## Restaurant task
def waiter(menu):
    menu = ["Chicken curry", "Vegetable curry", "Lamb curry", "Chips", "Chicken Wrap", "Veggie Wrap",
        "Dr Pepper", "Fanta", "Coke", "Water"]

    #  current_order = [] # first create an empty list
    # customer greeting
    print("Hello, thank you for entering our restaurant, what would you like to order?")
    while len(order)<3:  # you can only order three items
        order = input()   # input the order
        if order in menu:
            print("would you like to order anything else?")
            order.append(order) # adds to the order list
            print(f"So you have ordered {order}")
        else:
            print("item not in the menu") # if item not in menu print this


order = input()
waiter(order)

## Fizzbuzz
def x(range):
        for x in range(1,101):
          if(x%3==0 and x%5==0):
            print("FizzBuzz")
          elif(x%3 == 0):
            print("Fizz")
          elif(x%5 == 0):
            print("Buzz")
          else:
            print(x)
        return f"for every number divisible by 3 it returns fizz, and for 5 buzz and for both fizzbuzz"
print(x(range))