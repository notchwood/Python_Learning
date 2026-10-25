# tiy_9_8_privileges.py
class Users:
    """Modeling Users with personal attributes"""
    
    def __init__ (self, first_name, last_name, job, building, id_badge_num ):
        """Initializing attributes names"""
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job
        self.building_location = building
        self.badge_number = id_badge_num

    def describe_user(self):
        """Print persons name and attributes"""
        print(f"The user name is: {self.first_name} {self.last_name}")
        print(f"Job Title: {self.job_title}")
        print(f"located in building: {self.building_location}")
        print(f"Badge ID #: {self.badge_number}")

    def greet_user(self):
        """Greeting each user by name"""
        print(f"Hello {self.first_name}")

class Admin(Users):
    """Admin subclass """
    def __init__ (self, first_name, last_name, job, building, id_badge_num ):
        super(). __init__ (first_name, last_name, job, building, id_badge_num )
         
class Privileges(Admin):
    """ sub-subclass """
    def __init__ (self, first_name, last_name, job, building, id_badge_num ):
        super(). __init__ (first_name, last_name, job, building, id_badge_num )
        self.privileges = ["   can add post", "   can delete post", "   can ban users", "   can suspend accounts"]
    
    def show_privileges(self):
        """Method used to give admin privileges"""
        print(f"The following are privileges granted to {self.first_name}:")
        for privilege in self.privileges:
            print(privilege)

# Creating instance of admin (new object)
person_4 = Privileges("Arthur", "", "Admin", "infinity", "1")

# print person's name and attributes
person_4.describe_user()
person_4.greet_user()
person_4.show_privileges()