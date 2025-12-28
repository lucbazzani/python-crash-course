# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least
# three names of cats in the first file and three names of dogs in the second
# file. Write a program that tries to read these files and print the contents of
# the file to the screen. Wrap your code in a try-except block to catch the
# FileNotFound error, and print a friendly message if a file is missing. Move one
# of the files to a different location on your system, and make sure the code in
# the except block executes properly
from pathlib import Path 

def print_pet_names(path): 
    """Print the names of pets written in a file.""" 
    try: 
        names = path.read_text(encoding='utf-8') 
    except FileNotFoundError: 
        print(f"\nSorry, the file '{path}' was not found.\n")
        # Exercise 10-9: replace line 15 with 'pass'
    else: 
        lines = names.splitlines()
        print(f"Pet names found in '{path}':")
        for line in lines: 
            print(line)


filenames = ['basics/chapter_10_exercises/text_files/dogs.txt', 'basics/chapter_10_exercises/text_files/cats.txt']

for filename in filenames: 
    path = Path(filename) 
    print_pet_names(path)
    