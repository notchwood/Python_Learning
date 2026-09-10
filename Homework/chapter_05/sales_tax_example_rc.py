# My version of try 5-2. More Conditional test

import random

RUN_TIMES = 15

sales_tax_rate = 0.065
not_taxables = ["carrots", "lettuce", "ice Cream", "nothing found"] 
taxables = ["Wigit *", "shamPoo *", "tooth brush *"]

# prefix lc = lowercase - used for during comparisons, and using comprehension
# on lists
lc_non_cess_items = [food_item.lower() for food_item in not_taxables]
lc_cessed_items = [durable_item.lower() for durable_item in taxables]

# concatenate lowcass taxable and non taxable into one list 
lc_complete_list = lc_non_cess_items + lc_cessed_items

i = 0
while i < RUN_TIMES:
    i += 1
    print(f" TEST {i} ~~~~~~~~~~~~~~~~~~~~~~~")
    test = "pass"
    
    #items = lower_cased_items + taxables
    item = random.choice(lc_complete_list)

    if item in lc_non_cess_items:
        b_is_taxable = False
    else:
        b_is_taxable = True

    if item == "wigit *":
        price = 150
    elif item == "shampoo *":
        price = 9

    elif item == "carrots":
        price = 3

    elif item == "tooth brush *":
        price = 4

    elif item == "lettuce":
        price = 2

    elif item == "ice cream":
        price = 5

    elif item ==  "nothing found" :
        price = 0
        test = ("no item")
        print("You bought nothing")

    if test != "no item":
        print(f"You purchased: {item.title()}")

    if b_is_taxable == True:
        print(f"Subtotal:   ${price:.2f}")
        sales_tax = price * sales_tax_rate   
        sales_tax = price * sales_tax_rate
        print(f"Sales Tax:  ${sales_tax:.2f}")
        price = price + sales_tax
        print(f"Total cost: ${price:.2f}")
    elif b_is_taxable == False:
        if test != "no item":
            print(f"Total cost: ${price:.2f}")
            #print("non-taxable Item")
        else:
            print("Please buy something!")
    if price >= 100:
        print("Would you like that gift wrapped?")
