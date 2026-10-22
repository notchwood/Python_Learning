# tiy_9_4_number_served.py

class Restaurant:
    """Modeling opening a new restaurant"""
    
    def __init__ (self, restaurant_name, cuisine_type):
        """Initialize name and type of cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.count_served = 0

    def describe_restaurant(self):
        """Describe new restaurant"""
        print(f"The new restaurant, {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant (self):
        """Print that restaurant is now open"""
        print(f"{self.restaurant_name} is now open for business")

    def set_number_served (self):
        """self explanatory"""
        print(f"now seating the Jones's party of {self.count_served}")

    def replace_num_seated(self, seatings):
        """replacing seating w/ a parameter"""
        self.count_served = seatings

    def decrease_party(self):
        """example of augmented assignment"""
        self.count_served -= 3

    def reset_party_number(self, change_seating):
        """just having pure fun w/ this"""
        self.count_served += change_seating 

# Creating 1 instance (new object)
rest_1 = Restaurant("Wildwood", "Steak-house")

print(rest_1.restaurant_name)
print(rest_1.cuisine_type)

# opening restaurant announcement
rest_1.open_restaurant()

rest_1.describe_restaurant()

# Changing seating by attribute assignment 
rest_1.count_served = 9
rest_1.set_number_served()

#  replacing # of seating with an argument
rest_1.replace_num_seated(8)
rest_1.set_number_served()

# decreasing seating by augmented assignment in method
rest_1.decrease_party()
rest_1.set_number_served()

# combining rest.decrease_party and replace_num_seated
rest_1.reset_party_number(-2)
rest_1.set_number_served() 