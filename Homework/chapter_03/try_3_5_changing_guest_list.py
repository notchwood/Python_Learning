# try_3_5_changing_guest_list.py

guests = ["ronnie", "sally", "tony 'the tiger'", "woody Boyd" ]
for guest in guests:
    print(f"Dear {guest.title()}, I would be honored if you could join our friends tomorrow for a dinner party.\n")
canceled = guests.pop(1)
new_guest = "red o' leary".replace("o' ", "o'").title()
guests.append(new_guest)
print(f"Our friend {canceled.title()} can't make our gathering but {new_guest} will be joining us, in {canceled.title()}\n's place.")
for guest in guests:
    print(f"Dear {guest.title()}, I would be honored if you could join our friends tomorrow for a dinner party.\n")
