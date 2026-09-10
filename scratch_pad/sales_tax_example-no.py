# My version of try 5-2. More Conditional test
# Note: I credit idea from book: Python All-in-One For Dummies - Wiley & Sons

import random

sales_tax_rate = 0.065
non_taxables = ["carrots", "lettuce", "ice Cream", "nothing found"] 
taxables = ["Wigit *", "shamPoo *", "tooth brush *"]






raw_taxables = taxables
lower_cased_items = []


# non_taxables = non_taxables.lower()
# no_tax_lowedcases = [non_taxables.lower for item in non_taxables]
concated_raw_list = non_taxables + taxables
for item in concated_raw_list:
    item = [item.lower()]
    lower_cased_items = lower_cased_items + item

#print("START -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
i = 0
while i < 5:
    print(f" TEST {i} ~~~~~~~~~~~~~~~~~~~~~~~")
    test = "pass"
    i = i + 1
    #items = lower_cased_items + taxables
    item = random.choice(lower_cased_items)

    if item in lower_cased_items:
        taxable = False
    else:
        taxable = True

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
        print("no item found")

    if test != "no item":
        print(f"The item :{item.title()} will cost you")

    if taxable == True:
        print(f"Subtotal : ${price:.2f}")
        sales_tax = price * sales_tax_rate   
        print(f"Subtotal : ${price:.2f}")
        sales_tax = price * sales_tax_rate
        print(f"Sales Tax: ${sales_tax:.2f}")
        price = price + sales_tax
        print(f"Your price : ${price:.2f}")
    elif taxable == False:
        if test != "no item":
            print(f"Your price : ${price:.2f}")
            print("non-taxable Item")
        else:
            print("There is no charge")
    
