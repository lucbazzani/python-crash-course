# 10-4. Guest: Write a program that prompts the user for their name. When
# they respond, write their name to a file called guest.txt.
from pathlib import Path 

name = input("Hello! What is your name?\n")
print(f'\nWelcome {name.title()}!')
 
path = Path('basics/chapter_10_exercises/text_files/guest.txt') 
path.write_text(name)
