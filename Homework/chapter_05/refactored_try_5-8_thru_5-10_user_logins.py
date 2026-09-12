#from unittest import result

lc_users = [] # create a new list to store the lower case users
user = [] # used as an iteratorator through users tuple and store them in the lc_users
users = ("admin", "Mike", "deNise") # create a immutable tuple to store the users
TRIES = 3 

def test_user_credentials(worker_name):
    if worker_name in lc_users:
        if worker_name == "admin":
            print(f"Hi, {worker_name.title()} of I.T.. Hope you have a great day!")
        else:
            print(f"Hello, {worker_name.title()} have good day at work.")
        return True     
def list_valid_users():
    for lc_user in lc_users[:]:
        print(lc_user.title())

worker_name = input("Please enter your name: ")

for user in users:
    lc_input_name = user.lower()
    lc_users.append(lc_input_name)
worker_name = worker_name.lower()

for attempt in range(TRIES, 1, -1):
    result = test_user_credentials(worker_name)
    if result:
        break
    print(f"You have {attempt - 1} Tries left.")
    # for lc_user in lc_users[:]:
    #     print(lc_user.title())
    list_valid_users()
    worker_name = input("Please enter your name: ") 
    worker_name = worker_name.lower()   
else:
    for attempt in range(2, TRIES, 1):
        print(f'You have {attempt - 2} tries left.')
        result = test_user_credentials(worker_name)
        if result:
            break
        else:
            print("and You have exceeded the maximum number of tries." 
            " Please call your I.T admin!")

#
