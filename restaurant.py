def waiter(menu):
    menu = ["Chicken curry", "Vegetable curry", "Lamb curry", "Chips", "Chicken Wrap", "Veggie Wrap",
        "Dr Pepper", "Fanta", "Coke", "Water"]

    #  current_order = [] # first create an empty list
    # customer greeting
    print("Hello, thank you for entering our restaurant, what would you like to order?")
    while len(current_order)<3:  # you can only order three items
        order = input()   # input the order
        if order in menu:
            print("anything else?")
            current_order.append(order) # adds to the order list
            print(f"So you have ordered {current_order}")
        else:
            print("item not in the menu") # if item not in menu print this


order = input()
waiter(order)