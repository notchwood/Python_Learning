price_checking = True
while price_checking:
    #print("Type 'quit' when you are finished")
    age = int(input("\nHow old is the person that wants admitance to the movie? "))
   
    if age > 12:
        print("The ticket will cost $15 please.")
    elif age in range(3, 13):
        print("The ticket will cost $10 please")
    else:
        print("The ticket is free for children 3 years old and younger")
    print("\nType 'quit' when you are finished")

    print("Do you need anymore tickets?")
    answer = input("yes or no: ")
    if answer == "no":
        print("Thank you, have a nice day")
        #price_checking = False
        break

