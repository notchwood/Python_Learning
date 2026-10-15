# refactored_try_5-8_thru_5-10_user_logins.py
# eleminate counters and use "for" statements built in counts


users = ("admin", "Mike", "deNise") # create a immutable tuple to store the users
TRIES = 3
lc_users = [user.lower() for user in users] # Using comprehension for creating a new sequence (lc_users) - from list "users"

def test_user_credentials(login_a_user): # function to verify login attempt is a registered user
    if login_a_user in lc_users: # verifies login is in list of registerd users
        if login_a_user == "admin":
            print(f"Hi, {login_a_user.title()} of I.T.." 
                  "Hope you have a great day!")
        else:
            print(f"Hello, {login_a_user.title()} have good day at work.")
        return True 
    return False    
def list_valid_users(): # this function give the loggin client a list of registered users 
    print("Try using one of the following names:")

#########################################################################################################################################
    print([user.title()[:] for user in users]) # this statement does the same as the following but is this done using a slice [:] for all items
    print([user.title() for user in users]) # using conprehention in plance of "for" looping to print registered titled user's list of items
    # print(users.title()) # 'tuple' object has no attribute 'title' AttributeError: 'tuple' object has no attribute 'title'
    # print(users) # if this prints all the items in a tuple which can't use the method title() why?
    for user in users:
        print(user.title()) # why does this work in a for loop but not when used a print statement by it self. Referring two lines above does not work??? confused...
    # ^^ the above was me experimenting - looking at the mechanics of the this tuple "users" ^^
#######################################################################################################################################
  
for attempt in range(TRIES, 0, -1): # count down loop, of which two are for extra tries to login, excluding the zero int.
    login_a_user = input("Please enter your name: ").lower() 

    if test_user_credentials(login_a_user): 
        break # the break statement only gets executed if the function test_user_credentials return a boolean value of True
    print(f"Incorrect name. You have {attempt - 1} tries left.") # using "for" built in counter using the range from 3 - 1, using -1 as the step & excluding the 0 value delimitor in decending order   
    if attempt > 1:
        list_valid_users()               
else: # if the conditional is not met as True, then the eles statement is executed as a catch all for the main loop
    print("You have exceeded the maximum number of tries." 
        " Please call your I.T admin!") 
 