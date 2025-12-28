# 10-14. Verify User: The final listing for remember_me.py assumes either
# that the user has already entered their username or that the program is
# running for the first time. We should modify it in case the current user is not
# the person who last used the program.
# Before printing a welcome back message in greet_user(), ask the user if
# this is the correct username. If it’s not, call get_new_username() to get the
# correct username.
from pathlib import Path 
import json
 
def get_stored_username(path): 
    """Get stored username if available.""" 
    if path.exists(): 
        contents = path.read_text() 
        username = json.loads(contents) 
        return username 
    else: 
        return None

def get_new_username(path): 
    """Prompt for a new username.""" 
    username = input("What is your name?\n") 
    contents = json.dumps(username) 
    path.write_text(contents) 
    return username
 
def greet_user(): 
    """Greet the user by name.""" 
    path = Path('basics/chapter_10_exercises/text_files/username.json') 
    username = get_stored_username(path) 
    if username and is_correct_username(username):
        print(f"\nWelcome back, {username}!")        
    else: 
        username = get_new_username(path)
        print(f"\nWe will remember you when you come back, {username}!")

def is_correct_username(username):
    resp = input(f"Is '{username}' your username? (y/n)\n")
    if resp == 'y':
        return True
    else:
        return False


greet_user()