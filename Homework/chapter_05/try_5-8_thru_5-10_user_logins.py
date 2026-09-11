users = [] # create a list to store the users
lc_users = [] # create a new list to store the lower case users
user = [] # used as an iteratorator through users tuple and store them in the lc_users
users = ("admin", "mike", "denise") # create a immutable tuple to store the users
TRIES = 3 
    
worker_name = input("Please enter your name: ")
#c_users = []
for user in users:
    lc_input_name = user.lower()
    lc_users.append(lc_input_name)
worker_name = worker_name.lower()
i = 0
j = TRIES

while i < TRIES:
    i += 1
    if worker_name not in lc_users and j > 1:
        j = j - 1
        # This block is for demonstration purpose only. 
        # it would not be a good idea in the real world..
        print("Please try using one of following user names.")
        for lc_user in lc_users[:]:
            print(lc_user.title())
        print(f'You have {j} tries left.')
        worker_name = input("Please enter your name: ")
        if j == 1:
            print("You have exceeded the maximum number of tries." 
            " Please call your I.T admin!")
            break # I learned that "break" can only be used in "if" and "while" loops.
                  # but not "for" loops
    else:
        i = TRIES + 1 
        if worker_name == "admin":
            print(f"Hi, {worker_name.title()} of I.T.. Hope you have a great day!")
        else:
            print(f"Hello, {worker_name.title()} have good day at work.")
