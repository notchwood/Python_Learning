# tiy_7_1_rental_car.py
# I have put more than a day in to get this to work the way I envisioned
# but to no avail. I just can't figure out to enforce boundries for input values

# global_error_cnt = 1 # can't figure out how to enforce number if tries count

''' setting up dictionary #also note the Make of vehicles 
    (ie. ford...) not used in script'''
rentals = {
    'vhcl_1': ['ford','edge','suv'],
    'vhcl_2': ['chevy', 'silverado', 'truck'],
    'vhcl_3': ['toyota', 'tundra', 'truck'],
    'vhcl_4': ['chevy', 'blazer', 'suv'],
    'vhcl_5': ['dodge', 'charger', 'sedan'],
    'vhcl_6': ['ford', 'f150', 'truck'],
    'vhcl_7': ['dodge', 'darango', 'suv']
}
# can't figure out how to enforce number if tries count
# def error_msg(guard_rail):
#     while global_error_cnt not in (1, guard_rail):
#         print("you're out")
#         break
#     global_error_cnt += 1    
#     print("error - please try again")
#     # main()

platform = {
    '1': 'sedan',
    '2': 'suv',
    '3': 'truck'
}
guard_rail = len(platform) 

print('\nHi, What kind of rental car are we looking for today? ')
print(f"Would you like one of the following: ")

for key, value in platform.items():
    print(f"{key} {value}")

prompt1 = "Please enter a number the platform type \nof vehicle you want to rent: "
platform_number: str = input(prompt1)

# can't figure out how to enforce number if tries count
# for platform_number in not (1, guard_rail):
#     # global_error_cnt += 1
#     # error_msg()
#     global_error_cnt += 1
#     while global_error_cnt > 3:
#         break

# rummage through platform dict.
platform_type = platform.get(platform_number, " - You have entered a wrong number")

current_available = []
count = 0 # cars on hand inventory
for key, v_list in rentals.items():

    b_ans = platform_type in v_list[2]
    if b_ans:
        count += 1
        current_available.append(v_list[1])
    
print(f"We have {count} {platform_type.title()} for rent.")
        
model = {}
x = 0
for car in current_available:
    x += 1
    print(f"{str(x)} {car}")
    model.update({str(x): car})# = {x: car}

car_number: str = input("Enter a number for car you would like to rent. ")

model_name = model.get(car_number.title(), " - You have not pick a number from the display")
print(f"You have chosen a {model_name} {platform_type}. Enjoy you ride.")