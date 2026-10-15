# `tiy_7_cleanup.py`

# A list of vehicles with duplicate trade-ins clogging the lot
lot_inventory = ['suv', 'truck', 'sedan', 'suv', 'truck', 'suv']

print("Original inventory:", lot_inventory)

# THE CLEAN MECHANIC: As long as 'suv' exists anywhere in the list...
while 'suv' in lot_inventory:
    # ... find next 'vuv     and delete it
    if lot_inventory[3] == "truck":
        break
    lot_inventory.remove('suv')

    print("Cleanded invenrory: ", lot_inventory )