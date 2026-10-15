# boot_system.py
boot_system = True

while boot_system:
    # 1. Collect and preserve the raw input exactly how the user typed it
    racer_name = input("Enter a racer's name to register (or type 'exit'): ")

    # 2. Check the input with .lower() just for the gate evaluation
    if racer_name.lower() == 'exit':
        boot_system = False
    else:
        #3. The original casing (like 'MIke' or 'Denise') is perfecly preserved
        print(f"Welcome to the leaderboard, {racer_name}!\n")

    print("This is the input string, notice the casing is preserved: " + racer_name)
print("Registration closed.")