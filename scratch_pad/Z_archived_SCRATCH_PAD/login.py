lc_users = [] # create a new list to store the lower case users
user = [] # used as an iteratorator through users tuple and store them in the lc_users
users = ("admin", "Mike", "deNise") # create a immutable tuple to store the users
TRIES = 3
cnt_users = len(users)
# standardize registered users to lower case characters
for user in users:
    lc_input_name = user.lower()
    lc_users.append(lc_input_name)



print()

for attempt in (TRIES, 0, -1):
    
    worker_name = input("Please enter your name: ")
    worker_name = worker_name.lower()
    # checking if worker in list of users
    for worker_name in range (0, cnt_users, 1):
        lc_user in lc_users
        for worker_name in lc_user: 
            print(worker_name)