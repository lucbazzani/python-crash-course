# 10-5. Guest Book: Write a while loop that prompts users for their name.
# Collect all the names that are entered, and then write these names to a file
# called guest_book.txt. Make sure each entry appears on a new line in the
# file.
from pathlib import Path 

name = input("Hello! Please enter all of your names (enter \'q\' when you finish):\n")
guests = ''
while name != 'q'.lower():
    guests += name + '\n'
    name = input()
 
path = Path('basics/chapter_10_exercises/text_files/guest_book.txt') 
path.write_text(guests)
