# try_3_7_shrinking_list.py
import random 
guests = ["ronnie", "sally", "tony 'the tiger'", "woody Boyd" ] # initialized list guests

count = 0
index = 0 
''' the counter is for me to differentiate each sectional change of output 
for each guest's attendence'''

def guest_invitations(guests, int(count), index):
    guests = guests
    count = count
    index = index


    int(count) = int(count) + 1 
    print(f"Output # str(count) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for guest in guests:
        index = guests.index(guest)
        guest = guest.title()
        print(f"{guest}, Please join our friends tomorrow for a dinner.\n")
        guests[index] = guest
    return (guests, count, index)
   
guests, count, index = guest_invitations(guests, count, index) 
#count= guest_invitations(guests, count) 
#count, index = guest_invitations()

# Dinner guest that will not being attending
canceled = guests.pop(1) # removing sally from the list but saving the str for later use
count = guest_invitations(guests, count, index)

# New dinner guest
new_guest = "red o' leary".replace("o' ", "o'").title()
guests.append(new_guest)
print(f"**>> Our friend {canceled.title()} can't make our gathering but {new_guest} will be joining us, in {canceled.title()}\'s place. <<**\n")

count, index = guest_invitations(guests, count, index) 

guests.insert(2, "michelle")
guests.insert(4, "Big Bill")
guests.append("Vinnae")
print("Great news! We found a bigger table")
count = guest_invitations(guests, count) 

# print(f"{guests}")
num_elements = len(guests)
num_elements -= 2
i = 0
while i < num_elements:
    random(guests)