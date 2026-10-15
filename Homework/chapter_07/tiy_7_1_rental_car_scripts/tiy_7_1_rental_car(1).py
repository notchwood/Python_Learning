# tiy_7_1_rental_car.py

types_of_vehicales = ['sedan', 'SUV', 'pickup']
makes = ['ford', 'chevy', 'dodge', 'toyota' ]
colors = ['blue', 'white', 'black', 'red']

state = True
while state:
    print('\nHi, What kind of rental car are we looking for today? ')
    print(f"We have the following: ")
    for car_type in types_of_vehicales:
        print(car_type)
    pick_car_type = input("Please enter kind of car: ")
    state = pick_car_type in types_of_vehicales
    if pick_car_type != state:
        pick_car_type = input("please pick a type of car from list above or type quit: ")
    if pick_car_type == 'quit':
        break 

    print("\nIs there a particular 'Make' you would like")
    for car_make in makes:
        print(car_make)
    pick_auto_make = input("Please enter make of car: ")

    print(f"\nWe will deliver a rental, {pick_auto_make} {pick_car_type} to your front door.")


    # ('Is there a particular color you would like? (yes or no) ')
    # if ask_color == 'yes':
    #     print(f"Please choose from the following colors\n")
    #     for color in colors:
    #         print(color)
    #     picked_color = input("Enter your color ")

    #     print(f'Let me see if I can find you a {car_rental}')
    # print("Okay, lets find you a car.")