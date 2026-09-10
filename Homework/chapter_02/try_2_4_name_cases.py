# try_2_4_name_cases.py

formal_name = 'mr. James McGill'
print(f"1. {formal_name.lower()}")
print(f"2. {formal_name.upper()}")
formal_name = formal_name.removeprefix('mr. ')
print(f"3. {formal_name}")
print(f"4. {formal_name.title()}")
print(f"5. {formal_name.capitalize()}")
print(f"6. {formal_name.replace('James', 'Jake')}")
formal_name = (f"Mr. {formal_name}")
sir_name = formal_name.replace('Mr.', 'Sir.')
print(f"7. {sir_name}")
str_breakup = sir_name.split()
print(f"8. {str_breakup}") # should be ['Sir.', 'James', 'McGill']
print(f"9. {str_breakup[2]}, {str_breakup[1]}")

