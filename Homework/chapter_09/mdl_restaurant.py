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