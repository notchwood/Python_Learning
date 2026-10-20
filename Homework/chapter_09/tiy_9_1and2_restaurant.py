# tiy_9_1and2_restaurant.py

# create a model for a restaurant
class Restaurant:
    """Modeling opening a new restaurant"""
    
    def __init__ (self, restaurant_name, cuisine_type):
        """Initialize name and type of cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def discribe_restaurant(self):
        """Discribe new restaurant"""
        print(f"The new restaurant, {self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant (self):
        """Print that restaurant is now open"""
        print(f"{self.restaurant_name} is now open")

# Creating and instance (new object)
rest_1 = Restaurant("Foodies", "Italian")

print(rest_1.restaurant_name)
print(rest_1.cuisine_type)
rest_1.open_restaurant()
rest_1.discribe_restaurant()
