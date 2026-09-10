users = [] # going to test in for statment for empty list
users = ["admin", "Mike", "Denise"]


for user in users:
    lc_user = users.copy()
    lc_users = lc_user
    for lc_user in lc_users:
        
        

# lc_users = [user.lower .append for user in users]

        print(lc_users)
for check_user in lc_users:
    if check_user == "admin":
        print("Hi, Master of I.T.. Hope you have a great day")
    else:
        print(f"Hello, {check_user}, have good work day.")