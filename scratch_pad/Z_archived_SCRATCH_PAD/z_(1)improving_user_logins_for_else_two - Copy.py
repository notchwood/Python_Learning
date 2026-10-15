# refactored_try_5-8_thru_5-10_user_logins.py
# eleminate counters and use "for" statements built in counts

lc_users = [] # create a new list to store the lower case users
#user = [] # used as an iteratorator through users tuple and store them in the lc_users
users = ("admin", "Mike", "deNise") # create a immutable tuple to store the users
TRIES = 3
lc_users = [user.lower for user in users] # I was trying to do this in
#test_user_credentials(login_a_user) function, no wonder I was getting null array


#************************************************************************ 
def test_user_credentials(login_a_user):
    # #lc_users = [user.lower() for user in users[:]] 
    # lc_users = [user.append(user).lower() for user in users]
  
    # # for lc_user in lc_users:
    # #           lc_user = lc_user.lower

    if login_a_user in lc_users: # compare login input to registered user database
        if login_a_user == "admin":
            print(f"Hi, {login_a_user.title()} of I.T.." 
                  "Hope you have a great day!")
        else:
            print(f"Hello, {login_a_user.title()} have good day at work.")
        return True # from my perl days I don't rember ever thinking of being able to have multiple returns
        # never mind using the if statement to accomplish this feat.
    return False # explicitly returns False rather than defaulting out to "None"    
#************************************************************************

def list_valid_users():
    print("Try using one of the following names:")
    print([user.title()[:] for user in users]) # using conprehention in plance of manual "for" looping to print registered titled user's list
    for user in users[:]:
        print(user.title())

    #print([user.title() for user in users])
#************************************************************************

for attempt in range(TRIES, 0, -1): # count down loop, of which two are for extra tries to login, excluding the zero int.
    login_a_user = input("Please enter your name: ").lower() # get a persons login name and assign it to another str to prepare for a comparison registration accounts
                    # the lower() func to the input made the consoledated into one  makes more sence to me now


    if test_user_credentials(login_a_user):
            #login_a_user = input("Please enter your name: ").lower() # get a persons login name and assign it to another str to prepare for a comparison registration accounts
            # the lower() func to the input made the consoledated into one  makes more sence to me now
            # login_a_user = login_a_user.lower()
            # #for user in users:
        break

    if attempt > 1:
        list_valid_users() 
        #print(f"You have {attempt - 1} Tries left.") # commited out was splitting for from the else statement
      
else: # if all checks for registered users, this is last msg in code
             print("You have exceeded the maximum number of tries." 
        " Please call your I.T admin!") 










           # lc_users = [user.lower() for user in users] # I see the efficency, by elimating the middle man var."raw_emp_database" 
            # the "user" str is used to convert to low case char's then asigned to lc_user 
            # 1st creating a loop of users tuple list then
            # 2nd lower case the user from users list then
            # 3rd assign to lc_users a nutable list, that is only used in a for loop extractoin from LIST users
            # will be used for str. conversion to lower case.
            # note: NO COMPARISON MADE made with var
            # and the list[str] just showing of type annotations maybe helpful to me when following my own code
        
        # login_a_user = login_a_user.lower() # for standardizing to lower case char.s for conparision test