# try_3_6_more_guest.py

guests = ["ronnie", "sally", "tony 'the tiger'", "woody Boyd" ] # initialized list guests

count = 0 
''' the counter is for me to differentiate each sectional change of output 
for each guest's attendence'''

def guest_invitations(guests, count):
    count += 1 
    print(f"Output # {count} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for guest in guests:
        index = guests.index(guest)
        guest = guest.title()
        print(f"{guest}, Please join our friends tomorrow for a dinner.\n")
        guests[index] = guest
    return count    
count = guest_invitations(guests, count) 

# Dinner guest that will not being attending
canceled = guests.pop(1) # removing sally from the list but saving the str for later use
count = guest_invitations(guests, count)

# New dinner guest
new_guest = "red o' leary".replace("o' ", "o'").title()
guests.append(new_guest)
print(f"**>> Our friend {canceled.title()} can't make our gathering but {new_guest} will be joining us, in {canceled.title()}\'s place. <<**\n")

count = guest_invitations(guests, count) 

guests.insert(2, "michelle")
guests.insert(4, "Big Bill")
guests.append("Vinnae")
print("Great news! We found a bigger table")
count = guest_invitations(guests, count) 
print(f"There will be {len(guests)} at the dinner table.")
# print(f"{guests}")