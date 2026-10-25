# tiy_9_10_import_restaurant.py
from mdl_restaurant import Restaurant

# Creating 3 instance (new object)
rest_1 = Restaurant("Wildwood", "Steak-house")
rest_2 = Restaurant("Chilly's", "Mex-American")
rest_3 = Restaurant("McDonalds", "Fast-Food")

# restaurant Wildwood - attributes and methods
print(rest_1.restaurant_name)
print(rest_1.cuisine_type)
rest_1.open_restaurant()
rest_1.describe_restaurant()

# restaurant Chilly's - attributes and methods
print(rest_2.restaurant_name)
print(rest_2.cuisine_type)
rest_2.open_restaurant()
rest_2.describe_restaurant()

# restaurant McDonalds - attributes and methods
print(rest_3.restaurant_name)
print(rest_3.cuisine_type)
rest_3.open_restaurant()
rest_3.describe_restaurant()