# tiy_9_1and2_restaurant.py

# create a model for a restaurant
class Restaurant:
    """Modeling opening a new restaurant"""
    
    def __init__ (self, restaurant_name, cuisine_type):
        """Initialize name and type of cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe new restaurant"""
        print(f"The new restaurant, {self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant (self):
        """Print that restaurant is now open"""
        print(f"{self.restaurant_name} is now open")

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


