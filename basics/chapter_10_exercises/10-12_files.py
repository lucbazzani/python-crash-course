# 10-12. Favorite Number Remembered: Combine the two programs you
# wrote in Exercise 10-11 into one file. If the number is already stored, report
# the favorite number to the user. If not, prompt for the user’s favorite number
# and store it in a file. Run the program twice to see that it works.
from pathlib import Path
import json

def get_stored_favorite_number(path):
    """Get favorite number from a file if it exists, otherwise return None."""
    if path.exists():
        contents = path.read_text() 
        favorite_number = json.loads(contents) 
        return favorite_number
    else:
        return None

def prompt_new_favorite_number(path):
    """Prompt for a favorite number, store it, and return it.""" 
    favorite_number = input("What is your favorite number?\n")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    return favorite_number

def print_users_favorite_number():
    """Display the user's favorite number or prompt for it."""
    path = Path('basics/chapter_10_exercises/text_files/favorite_number.json') 
    favorite_number = get_stored_favorite_number(path)
    if favorite_number:
        print(f"Your favorite number is {favorite_number}.")
    else:
        favorite_number = prompt_new_favorite_number(path)
        print(f"\nI will remember that your favorite number is {favorite_number}.")


print_users_favorite_number()
