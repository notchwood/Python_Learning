
class Users:
    """Modeling Users with personal attributes"""
    
    def __init__ (self, first_name, last_name,age, eye_color, hair_color ):
        """Initializing attributes names"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color

    def describe_user(self):
        """Print persons name and attributes"""
        print(f"The user name is: {self.first_name} {self.last_name}")
        print(f"age: {self.age}")
        print(f"eye color: {self.eye_color}")
        print(f"hair color: {self.hair_color}")

    def greet_user(self):
        """Greeting each user by name"""
        print(f"Hello {self.first_name}")

# Creating 1 instance (new object)
person_1 = Users("Mike", "Jones", "75", "green", "white" )
person_2 = Users("Pual", "Smith", "62", "blue", "grey" )
person_3 = Users("Denise", "Peterson", "49", "brown", "Pink" )

# print person's name and attributes
person_1.describe_user()
person_1.greet_user()
print()
person_2.describe_user()
person_2.greet_user()
print()
person_3.describe_user()
person_3.greet_user()    