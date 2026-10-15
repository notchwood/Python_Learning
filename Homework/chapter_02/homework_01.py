# Homework 1 - Chapter 2
name = "mR. boe  JAngles  !"
print(f"clean up the name: {name} \n")
cleaned_name = name.strip().lower().replace("mr.", "").title() .replace("!", "")
print(f"cleaned name: {cleaned_name}")
create_a_list = cleaned_name.split()
print(f'list of cleaned elements: {create_a_list}')
print(f" reorder list elements: {create_a_list[1]}, {create_a_list[0]}") 
