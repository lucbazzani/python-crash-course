# 10-11. Favorite Number: Write a program that prompts for the user’s
# favorite number. Use json.dumps() to store this number in a file. Write a
# separate program that reads in this value and prints the message I know
# your favorite number! It’s _____."
from pathlib import Path 
import json
 
path = Path('basics/chapter_10_exercises/text_files/favorite_number.json') 
contents = path.read_text() 
favorite_number = json.loads(contents) 
 
print(f"Your favorite number is {favorite_number}.")
