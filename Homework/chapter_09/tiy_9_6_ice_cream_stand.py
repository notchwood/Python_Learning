
# create a model for a restaurant
class Restaurant:
    """Modeling opening a new restaurant"""
    
    def __init__ (self, restaurant_name, cuisine_type):
        """Initialize name and type of cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe new restaurant"""
        print(f"The new restaurant, {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant (self):
        """Print that restaurant is now open"""
        print(f"{self.restaurant_name} is now open for business")

class IceCreamStand(Restaurant):
    def __init__ (self, restaurant_name, cuisine_type):
        super(). __init__ (restaurant_name, cuisine_type)
        
        self.flavors = ["  chocolate", "  rocky road", "  vanilla", "  strawberry", "  cookie dough"]

    def print_flavors(self):
        choose_flavor = len(self.flavors)
        print(f"Pick from our {choose_flavor} flavors")
        for flavor in self.flavors:
            print(flavor)

# Creating 3 instance (new object)
rest_1 = Restaurant("Wildwood", "Steak-house")
rest_2 = Restaurant("Chilly's", "Mex-American")
rest_3 = Restaurant("McDonalds", "Fast-Food")
rest_4_ics = IceCreamStand("Friendly's", "Iced-Cream")

print(rest_4_ics.restaurant_name)
print(rest_4_ics.cuisine_type)
rest_4_ics.open_restaurant()
rest_4_ics.describe_restaurant()
rest_4_ics.print_flavors()
print()

# restaurant Wildwood - attributes and methods
print(rest_1.restaurant_name)
print(rest_1.cuisine_type)
rest_1.open_restaurant()
rest_1.describe_restaurant()
print()

# restaurant Chilly's - attributes and methods
print(rest_2.restaurant_name)
print(rest_2.cuisine_type)
rest_2.open_restaurant()
rest_2.describe_restaurant()
print()

# restaurant McDonalds - attributes and methods
print(rest_3.restaurant_name)
print(rest_3.cuisine_type)
rest_3.open_restaurant()
rest_3.describe_restaurant()
print()
