order_toppings = []
order = True
while order:
    print("Please enter your pizza topping here. Type 'quit' when you are finished")
    topping = input("What kind of topping would you like? ")
    order_toppings.append(topping)
    if topping == 'quit':
        print("Thank you for your order")
        order = False
print(order_toppings)
