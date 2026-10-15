# refactored_try_5-8_thru_5-10_user_logins.py
# eleminate counters and use "for" statements built in counts

lc_users = [] # create a new list to store the lower case users
user = [] # used as an iteratorator through users tuple and store them in the lc_users
users = ("admin", "Mike", "deNise") # create a immutable tuple to store the users
TRIES = 3 

def test_user_credentials(login_a_user):
    if login_a_user in lc_users: # compare login input to user database
        if login_a_user == "admin":
            print(f"Hi, {login_a_user.title()} of I.T.." 
                  "Hope you have a great day!")
        else:
            print(f"Hello, {login_a_user.title()} have good day at work.")
        return True     
def list_valid_users():
    print("Try using one of the following names:")
    for lc_user in lc_users[:]: # list from from lc_users database
        print(lc_user.title())
    print(list(users)) # I just thought it was quicker to look @ during debugging
    print(f"You have {attempt - 1} Tries left.")
login_a_user = input("Please enter your name: ")
for user in users:
    raw_emp_database = user.lower() # for standardizing to lower case char.s for conparision test
    lc_users.append(raw_emp_database) # new list to compair to 
login_a_user = login_a_user.lower() # for standardizing to lower case char.s for conparision test
for attempt in range(TRIES, 0, -1):
    result = test_user_credentials(login_a_user)
    if result: # boolean value, actually "None" value is returned by "test_user_credentials(login_a_user)""
        break # success we have a registed user
    if attempt > 1: # inclued the last two tries at inputing a registered user
        #print(f"You have {attempt - 1} Tries left.")
        list_valid_users() # list out current registered users & count how many inputs are left
        login_a_user = input("Please enter your name: ") 
        login_a_user = login_a_user.lower()   
    else: # if all checks for registered users, this is last msg in code
        print("and You have exceeded the maximum number of tries." 
        " Please call your I.T admin!")