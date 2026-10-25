# flag start

from mdl_Admin_Privileges_9_12 import Admin

# tiy_9_8_privileges.py

# Creating instance of admin (new object)
person_4 = Admin("Arthur", "", "Admin", "infinity", "1")

# print person's name and attributes
person_4.describe_user()
person_4.greet_user()
print(f"The following are privileges granted to {person_4.first_name}:")

person_4.privileges.show_privileges()