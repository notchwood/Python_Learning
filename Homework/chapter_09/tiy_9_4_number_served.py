# 
# tiy_9_4_number_served.py


class Restaurant:

    def __init__(self, name, cuisine_type):
        self.restaurant_name = name
        self.describe = cuisine_type

    def describe_restaurant(self):
        """Describe new restaurant"""
        print(f"The new restaurant, {self.restaurant_name} serves {self.describe}")

    def open_restaurant(self):
        """Print that restaurant is now open"""
        print(f"{self.restaurant_name} is now open")

rest_1 = Restaurant("Wildwood", "Steak-house")

print(rest_1.restaurant_name)
print(rest_1.describe)
rest_1.describe_restaurant()
rest_1.open_restaurant()


