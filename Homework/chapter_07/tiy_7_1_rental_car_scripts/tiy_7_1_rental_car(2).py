# tiy_7_1_rental_car.py

types_of_vehicales = ['sedan', 'SUV', 'pickup']
makes = ['ford', 'chevy', 'dodge', 'toyota' ]
colors = ['blue', 'white', 'black', 'red']

rentals = {
    'vhcl_1': ['ford','edge','suv'],
    'vhcl_2': ['chevy', 'silverado', 'truck'],
    'vhcl_3': ['toyota', 'tundra', 'truck'],
    'vhcl_4': ['chevy', 'blazer', 'suv'],
    'vhcl_5': ['dodge', 'charger', 'sedan'],
    'vhcl_6': ['ford', 'f150', 'truck'],
    'vhcl_7': ['dodge', 'darango', 'suv']
}

# for k, v in rentals.items():
#     #print(k, v)
#     #print(v[1])
#     b_ans = 'truck' in v[2]
#     if b_ans:
#         print(v[1])
#         print("this is it", b_ans)


# badge = (rentals[])
# print(badge)

# vic = input('pick a platform ')
# count = 0
# for vehicle, make, model, plat in rentals.items():
#     for make, model, plat in badging:
#         if plat == vic:
#             count += 1
#             print(vehicle, make, model, plat)


 


# plate_match = rentals.items()
# print(plate_match)
# # print(rentals)





# state = True
# while state:
print('\nHi, What kind of rental car are we looking for today? ')
print(f"Would you like one of the following: ")
print("a sedan, a suv or a truck")


number = str(input("pick a platform and enter a the number: "))


if number == '1':
    picked_platform = 'sedan'
elif number == '2':
    picked_platform = 'suv'
elif number == '3':
    picked_platform = 'truck'
#picked_platform = input('please enter here: ')

if number in range(1, 4):
    for key, v_list in rentals.items():
        #print(key, v_list)
        #print(v_list[1])
        b_ans = picked_platform in v_list[2]
        if b_ans:
            print(v_list[1])
            #print("this is it", b_ans)
else:
    print("start again")


#     for car_type in types_of_vehicales:
#         print(car_type)
#     pick_car_type = input("Please enter kind of car: ")
#     state = pick_car_type in types_of_vehicales
#     if pick_car_type != state:
#         pick_car_type = input("please pick a type of car from list above or type quit: ")
#     if pick_car_type == 'quit':
#         break 

#     print("\nIs there a particular 'Make' you would like")
#     for car_make in makes:
#         print(car_make)
#     pick_auto_make = input("Please enter make of car: ")

#     print(f"\nWe will deliver a rental, {pick_auto_make} {pick_car_type} to your front door.")


#     # ('Is there a particular color you would like? (yes or no) ')
#     # if ask_color == 'yes':
#     #     print(f"Please choose from the following colors\n")
#     #     for color in colors:
#     #         print(color)
#     #     picked_color = input("Enter your color ")

#     #     print(f'Let me see if I can find you a {car_rental}')
#     # print("Okay, lets find you a car.")