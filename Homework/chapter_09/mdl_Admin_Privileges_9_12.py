#Flag 2
from Users import Users
       
class Privileges:
    """  """
    def __init__ (self):
        
        self.privileges = ["   can add post", "   can delete post", "   can ban users", "   can suspend accounts"]
    
    def show_privileges(self):
        """Method used to give admin privileges"""
        #print(f"The following are privileges granted to {self.first_name}:")
        for privilege in self.privileges:
            print(privilege)

class Admin(Users):
    """Admin subclass """
    def __init__ (self, first_name, last_name, job, building, id_badge_num ):
        super(). __init__ (first_name, last_name, job, building, id_badge_num )

        self.privileges = Privileges()