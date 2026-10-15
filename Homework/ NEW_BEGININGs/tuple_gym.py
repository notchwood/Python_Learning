# # 1. Create a tuple containing fixed categories. 
# # Index 0 is a string, Index 1 is a mutable list [] of your actual network storage folders!
# nas_backup = ('Synology_DS720+', ['photos', 'scripts', 'documents'])

# # 2. Try to change the NAS name (Index 0) -> This will FAIL
# # nas_backup[0] = 'MyNAS_2023'

# # 3. Read the list inside the tuple by targeting Index 1
# print("Current shared folders:", nas_backup[1])

# # 4. UPDATE the list INSIDE the tuple! 
# # We target the list at index 1, and use our trusty .append() method
# nas_backup[1].append('ai_models')

# # 5. Read the tuple again to see the modification
# print("Updated shared folders after doing an append:", nas_backup[1])


# 1.
nas_backup = ('Synology_DS720+', ['photos', 'scripts', 'documents'])

# 2.
#nas_backup[0] = 'MyNas_2023' # This will FAIL because tuples are immutable

# 3. this will print the list inside of the tuple
print('current shared folders:', nas_backup[1])

# 4.
nas_backup[1].append('Ai_model')

# 5.
print('updated shared folders after doing an append:', nas_backup[1])

