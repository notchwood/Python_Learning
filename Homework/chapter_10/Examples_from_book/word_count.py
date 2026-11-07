from pathlib import Path

ABSOLUTE_PATH = "/volume1/DevDrive/Python_Learning/Homework/chapter_10/text_files/"

def count_words(file):
    """Count the approximate number of words in a file."""
    
    try:
        file_path = Path(f"{ABSOLUTE_PATH}{file}")
        contents = file_path.read_text(encoding='utf-8')
    
    except FileNotFoundError:
        pass
        #print(f"{file} File was not found\n")
            
    else:
        print(f"we found the file {file}")
        # Count the approximate number of words in the file:
        words = contents
        num_words = len(words)
        print(f"The file {file} has about {num_words} words\n")
        return num_words

filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt", "little_women.txt"]

for file in filenames:
    count_words(file)


 