# tiy_10_5_guest_book.py pg 192
from pathlib import Path
path = Path("/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/guestbook.txt")
list_of_names = ""
while True:
    name = input("Please enter your name:\n")
    if name == "quit":
        break
    list_of_names += (f"{name}\n")
path.write_text(list_of_names)
entry = path.read_text()
print(path)