class Users:
    """Modeling Users with personal attributes"""
    
    def __init__ (self, first_name, last_name, job, building, id_badge_num ):
        """Initializing attributes names"""
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job
        self.building_location = building
        self.badge_number = id_badge_num
        self.login_attempts = 0
        self.add_plural = ""

    def describe_user(self):
        """Print persons name and attributes"""
        print(f"The user name is: {self.first_name} {self.last_name}")
        print(f"Job Title: {self.job_title}")
        print(f"located in building: {self.building_location}")
        print(f"Badge ID #: {self.badge_number}")

    def greet_user(self):
        """Greeting each user by name"""
        print(f"Hello {self.first_name}")

    def increment_login_attempts(self):
        """ """
        self.login_attempts += 1 

    def reset_login_attempts(self):
         """ """
         self.login_attempts = 0

    def login_count(self):
        """ """
        if self.login_attempts != 1:
            self.add_plural = "s"
        print(f"{self.first_name} {self.last_name} has attempted to login {self.login_attempts} time{self.add_plural}") 

class Admin(Users):
    def __init__ (self, first_name, last_name, job, building, id_badge_num ):
        super(). __init__ (first_name, last_name, job, building, id_badge_num )
        self.privileges = ["   can add post", "   can delete post", "   can ban users", "   can suspend accounts"]
   
    def show_privileges(self):
        """"""
        print(f"The following are privileges granted to {self.first_name}:")
        for privilege in self.privileges:
            print(privilege)
        


# Creating 1 instance (new object)
person_1 = Users("Mike", "Jones", "Sr. SQE", "green", "2000" )
person_2 = Users("Paul", "Smith", "Vice President", "blue", "1000" )
person_3 = Users("Denise", "Peterson", "Marketing", "brown", "5000" )
person_4 = Admin("Arthur", "", "Admin", "infinity", "1")
# person_4 = Users("Arthur", "", "Admin", "infinity", "1")

# print person's name and attributes
person_4.describe_user()
person_4.greet_user()
person_4.show_privileges()



# print person's name and attributes
print()
person_1.describe_user()
person_1.greet_user()

# following the a persons login attempts, then print attempt counts
person_1.increment_login_attempts()
person_1.login_count()
person_1.increment_login_attempts()
person_1.login_count()

# resetting login attempt count then verifing count reset to zero
person_1.reset_login_attempts()
person_1.login_count()

print()
person_2.describe_user()
person_2.greet_user()

print()
person_3.describe_user()
person_3.greet_user()