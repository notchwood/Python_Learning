# Examples from pg 187 -189
from pathlib import Path

# Build a single string containing all the digits in pi_digits.txt

path = Path("/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/pi_digits.txt")
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:

    # This leaves the spaces that are in the pi_digit.txt file
    #pi_string += line

    # This strip out a lead and trailing white spaces
    #pi_string += line.strip()
    
    # This strips out all trailing white spaces.
    pi_string += line.lstrip()

print("\nHere is one long string created from list")
print(pi_string)
print(f"The length of the string is {len(pi_string)} long.")


