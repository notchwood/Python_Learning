from pathlib import Path

path = Path("/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/Python_learned.txt")

contents = path.read_text()
lines = contents.splitlines()
print(lines)

content_clean = ''
for line in lines:
    content_clean += f"{line}\n" 
    print(content_clean)

