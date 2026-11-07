# example from pg 184 - 187
from pathlib import Path

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@                                    @
#@ https://ehmatthes.github.io/pcc_3e @
#@                                    @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# NOT able to get relative paths to work!
#path = Path('Python_Learning/Homework/chapter_10/text_files/pi_digits.txt')
#path = Path('pi_digits.txt')

# for some reason I can only get absolute paths to work
path = Path("/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/pi_digits.txt")

print(f"\nThis is the what the variable path is set to:\n{path}\n")
print("Results from reading pi_digits.txt (note the extra line as output)")
contents = path.read_text()
print(contents)

# Since the read_text() leaves an extra empty line at the of the output, so you must
# strip it out if you want it to look exactly like the file
print("Example of remove extra, empty line")
contents = contents.rstrip()
print(contents)

# method chaining
contents = path.read_text().rstrip() # two methods, one line of code.

# use splitlines() method to turn long strings into a set of lines
print("Example of using the .splitlines() method.")
contents = path.read_text()
lines = contents.splitlines()
print(lines)
for line in lines:
    print(line)

