# 10-11. Favorite Number: Write a program that prompts for the user’s
# favorite number. Use json.dumps() to store this number in a file. Write a
# separate program that reads in this value and prints the message I know
# your favorite number! It’s _____."
from pathlib import Path 
import json
 
favorite_number = input("What is your favorite number?\n") 
 
path = Path('basics/chapter_10_exercises/text_files/favorite_number.json') 
contents = json.dumps(favorite_number)
path.write_text(contents)
print(f"\nI will remember that your favorite number is {favorite_number}.")
