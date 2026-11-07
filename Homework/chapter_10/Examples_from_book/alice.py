# alice.py
from pathlib import Path

path = ""
# un REM the line below if you want to skip the excpetion
path = "/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/" 

file = "alice.txt"
absolute_file_path = Path(f"{path}{file}")
try:
    contents = absolute_file_path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"{file} File was not found")
    # print(path)
else:
    print("we found the file")
    # Count the approximate number of words in the file:
    words = contents
    num_words = len(words)
    print(f"The file {file} has about {num_words} words")