import random

item = ""

items = ["wigit *", "carrots", "shampoo *", "lettuce", "ice cream", 'tooth brush *']
item = random.choice(items)
print(f"The item :{item} will cost you")
if "*" in item:
    taxable = True
else:
    taxable = False
total = 10
sales_tax_rate = 0.065
# Credit: following block of code from 
# Python All-in-One For Dummies - Wiley & Sons
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total      : ${total:.2f}")