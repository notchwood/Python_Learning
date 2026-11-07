from pathlib import Path
# the following comes from example script
#file_reader.py

path = Path("/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/pi_digits.txt")

# use splitlines() method to turn long strings into a set of lines
print("Example of using the .splitlines() method.")
contents = path.read_text()
# lines = contents.splitlines()
# print(lines)
for line in contents.splitlines():
    print(line)