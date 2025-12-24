# 8-12. Sandwiches: Write a function that accepts a list of items a person
# wants on a sandwich. The function should have one parameter that collects
# as many items as the function call provides, and it should print a summary
# of the sandwich that’s being ordered. Call the function three times, using a
# different number of arguments each time.
print('### EXERCISE 8-12 ###')
def make_sandwich(*items): 
    """Summarize the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:") 
    for item in items: 
        print(f"- {item}") 
 
make_sandwich('cheese')
make_sandwich('homus', 'onion', 'tomato')
make_sandwich('cream cheese', 'olive')

# 8-13. User Profile: Start with a copy of user_profile.py from page 148.
# Build a profile of yourself by calling build_profile(), using your first and last
# names and three other key-value pairs that describe you.
print('\n### EXERCISE 8-13 ###')
def build_profile(first, last, **user_info):
    """Builds a user profile dictionary."""
    user_info['first_name'] = first 
    user_info['last_name'] = last 
    return user_info 
 
my_profile = build_profile('lucas', 'bazzani', 
                             location='brazil', 
                             professional_goal='be a python developer',
                             hobbies = ['play drums', 'read books', 'hang out with friends']) 
print(my_profile)


# 8-14. Cars: Write a function that stores information about a car in a
# dictionary. The function should always receive a manufacturer and a model
# name. It should then accept an arbitrary number of keyword arguments. Call
# the function with the required information and two other name-value pairs,
# such as a color or an optional feature. Your function should work for a call
# like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly
print('\n### EXERCISE 8-14 ###')
def make_car(manufacturer, model, **car_info):
    """Creates a dictionary representing a car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# Fun Fact: 
# In Brazil, a Fiat Uno with a ladder on top is considered the fastest vehicle on Earth
the_goat_car = make_car(manufacturer = 'fiat', model = 'uno', color = 'white', year = 2008, has_ladder_on_top = True)
print(the_goat_car)
