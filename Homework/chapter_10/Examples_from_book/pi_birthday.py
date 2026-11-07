# Example on Pg. 189
from pathlib import Path

path = Path("/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/pi_million_digits.txt")

lines = path.read_text()
pi_string = ''
for line in lines:
    pi_string += line.strip()
#09161957print(pi_string)

birthday = input("Enter your birthday in this format mmddyyyy\n")

if birthday in pi_string:
    print("Your birthday appears int the first million digits of pi")
else:
    print("Your birthday does not appear in first million digits of pi")    