from pathlib import Path

# path = Path('pi_digits.txt')
path = Path('Homework/chapter_10/text_files/pi_digits.txt')

# import os
# print("CWD:", os.getcwd())
# # moved file "pi_digits.txt" to working VS_Code working directory  \Python_Learning 
# path = Path(__file__).resolve().parent / "pi_digits.txt"

# Set var path using absolute file path
path = Path("/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/pi_digits.txt")
print(f"\nThe following is the path to pi_digits.txt:\n {path} \n")
contents = path.read_text(encoding="utf-8")
contents = contents.rstrip()

print()
print(contents)

print("\nOutput is printed on one line")
pi_string = ''
lines = contents.splitlines()
for line in lines:
    pi_string += line
print(pi_string)



# Remove white spaces
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)

print(f"the length of pi_string is: {len(pi_string)}")
clean_pi_string = pi_string.strip()
print(clean_pi_string)


# path = Path("/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/pi_million_digits.txt")
# content = path.read_text()
# lines = content.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# birthday = str("101657")
# if birthday in pi_string:
#     print("yes")
# else:
#     print("no")

