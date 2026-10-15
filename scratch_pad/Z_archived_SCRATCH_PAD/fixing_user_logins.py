#
# fixing_user_logins.py - trying to get the code more efficiant
# by getting the last else block in line w/ tthe proceeding IF statement.

lc_users = [] # create a new list to store the lower case users
user = [] # used as an iteratorator through users tuple and store them in the lc_users
users = ("admin", "Mike", "deNise") # create a immutable tuple to store the users
TRIES = 3
#@@@@@@@@@@@@@@@@ DON'T TOUCH @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
for user in users:
    lc_input_name = user.lower()
    lc_users.append(lc_input_name)
 
#@@@@@@@@@@@@@@@@ DON'T TOUCH @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def test_user_credentials(worker_name):
    if worker_name in lc_users:
        print(f"Hi, {worker_name.title()} of I.T.. Hope you have a great day!")
    else:
        print(f"Hello, {worker_name.title()} have good day at work.")
        return True     
# def list_valid_users():
#     for attempt in lc_users[:]:
#         print(lc_user.title())
#         print(f"You have {attempt - 1} Tries left.")

#@@@@@@@@@@@@@@@@ DON'T TOUCH @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#****INPUT*****************************************
# worker_name = input("Please enter your name: ")
# worker_name = worker_name.lower()


for attempt in range(TRIES, 1, -1):

   worker_name = input("Please enter your name: ")
   worker_name = worker_name.lower()

    #result = test_user_credentials(worker_name)
#@@@@@@@@@@@@@@@@ DON'T TOUCH @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#     

    
 
    
    attempt = attempt - 1
    print(f"You have {attempt} Tries left.")

    for lc_user in lc_users[:]:
        print(lc_user.title())
    
        result = test_user_credentials(worker_name)
        if result:
            break    
            


#def list_valid_users():
for lc_user in lc_users[:]:
        print(lc_user.title())
        print(f"You have {attempt - 1} Tries left.")

    #list_valid_users() # I realized I realy need the function
    #attempt_temp = attempt - 1
for lc_user in lc_users[:]:
        print(lc_user.title())
print(f"You have {attempt - 1} Tries left.")   

#else:
for attempt in range(2, TRIES, 1):
        print(f'You have {attempt - 2} tries left.')
        result = test_user_credentials(worker_name)
        # if result:
        #     break
#else:
        print("and You have exceeded the maximum number of tries." 
            " Please call your I.T admin!")

 












# #****INPUT*****************************************         
#     worker_name = input("Please enter your name: ") 
#     worker_name = worker_name.lower()
# #^^^^CLEAN UP WORKER NAME^^^^^^^^^^^^^^^^^^^^^^^^^
       
# else:
#     for attempt in range(2, TRIES, 1):
#         print(f'You have {attempt - 2} tries left.')
#         result = test_user_credentials(worker_name)
#         if result:
#             break
#         else:
#             print("and You have exceeded the maximum number of tries." 
#             " Please call your I.T admin!")
