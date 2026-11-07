#_message.py - example from book
# Example from pg 190
from pathlib import Path
absolute_path = "/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/"
path = Path(f"{absolute_path}programming.txt")
path.write_text("I love to program with Python")


contents = path.read_text()
contents += "\nI love writing new programs"
contents += "\nI find coding creative"
contents += "\nI find coding to be rewarding"
print(contents)


# note: the write_text() can only write strings, not intergers (int)

# writing multiple lines to a file

# The following is not part of the example, but I want to see the
# output of the file created and what is in the new file.

# if "love" in contents:    
#     for string in contents.split():
#         replaced_string = string.replace("love", "hate")
#         print(replaced_string)