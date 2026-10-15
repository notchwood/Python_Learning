# shopping list management

shopping_list = [] # initialize

pickup_list = ['milk', 'eggs', 'bread', 'apples']

for item in pickup_list:
    shopping_list.append(item)
    print(f"{item} has been added to the list")
shopping_list.append('coffee') 
cross_off = shopping_list.index('bread')
shopping_list.remove('bread')


shopping_list.append('bananas')


shopping_list.remove('apples')
print("Apples marked as purchased")
print()


  