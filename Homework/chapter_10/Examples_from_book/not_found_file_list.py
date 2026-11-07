# This is my OWN EXPERIMENT!
from pathlib import Path

ABSOLUTE_PATH = "/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/"

def count_words(file, no_file_path):
    """Count the approximate number of words in a file."""
    
    try:
        contents = Path(f"{ABSOLUTE_PATH}{file}").read_text(encoding='utf-8')
    except FileNotFoundError:
        # Hiding the exception from the end user file was not found but 
        # writing the exception to a file.
        # print(f"{file} File was not found\n")
        # Print list of missing book content to a file
        string = f"{file} Not found!\n" + no_file_path.read_text()
        no_file_path = Path(f"{ABSOLUTE_PATH}Not_Found.txt").write_text(string)
    else:
        print(f"The file {file} was found and has about {len(contents)} words\n")
    
# This is a list of books contents (words)   
filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt", "Python_Crash_course.txt"]
no_file_path = Path(f"{ABSOLUTE_PATH}Not_Found.txt")
no_file_path.write_text("")
# string = ""
#no_file_path = Path(f"{ABSOLUTE_PATH}Not_Found.txt").write_text(no_file_path)
for file in filenames:
    count_words(file, no_file_path)
print(f"Check not found file(s):\n{no_file_path}")