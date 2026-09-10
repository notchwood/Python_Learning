# try_3_7_shinking_list.py

guests = ["ronnie", "sally", "tony 'the tiger'", "woody Boyd" ] # initialized list guests

count = 0 
''' the counter is for me to differentiate each sectional change of output 
for each guest's attendence'''

def guest_invitations(guests, count):
    count += 1 
    print(f"\nOutput # {count} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for guest in guests:
        index = guests.index(guest)
        guest = guest.title()
        print(f"{guest}, Please join our friends tomorrow for a dinner.")
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

'''print('Bad news, only 2 can come for dinner')
num_guest = len(guests)
while num_guest > 2:
    guests.pop(-1)
    num_guest -= 1
count = guest_invitations(guests, count)'''

print('Bad news, only 2 can come for dinner')
num_guest = len(guests)
uninvited = []
while num_guest > 2:
    uninvited.append(guests.pop(-1))
    num_guest -= 1
count = guest_invitations(guests, count)
print("We're having a heaping plate of spagetti code for dinner. Bon Appétit")
list = " - ".join(uninvited)
print(f"Sorry, {list}, I can only invite two by lottery.")
# print(f"{guests}")
