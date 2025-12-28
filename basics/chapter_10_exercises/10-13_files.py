# 10-13. User Dictionary: The remember_me.py example only stores one
# piece of information, the username. Expand this example by asking for two
# more pieces of information about the user, then store all the information you
# collect in a dictionary. Write this dictionary to a file using json.dumps(), and
# read it back in using json.loads(). Print a summary showing exactly what
# your program remembers about the user.
from pathlib import Path 
import json
 
def get_stored_user_info(path): 
    """Get stored user info if available.""" 
    if path.exists(): 
        contents = path.read_text() 
        user_info = json.loads(contents) 
        return user_info 
    else: 
        return None

def get_new_user_info(path): 
    """Prompt for a new user info.""" 
    first_name = input("Enter your first name:\n")
    last_name = input("\nEnter your last name:\n")
    favorite_game = input("\nEnter your favorite game:\n")
    user_info = {
        'first_name': first_name,
        'last_name': last_name,
        'favorite_game': favorite_game
    }

    contents = json.dumps(user_info) 
    path.write_text(contents) 
    return user_info 
 
def greet_user(): 
    """Greet the user by name.""" 
    path = Path('basics/chapter_10_exercises/text_files/user_info.json') 
    user_info = get_stored_user_info(path) 
    if user_info: 
        print(f"Welcome back, {user_info['first_name']} {user_info['last_name']}!")
        print(f"Lets play {user_info['favorite_game']} together!")
    else: 
        user_info = get_new_user_info(path)
        print(f"\nWe will remember your info when you come back, {user_info['first_name']}!")


greet_user()
