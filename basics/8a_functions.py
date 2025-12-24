# 8-1. Message: Write a function called display_message() that prints one
# sentence telling everyone what you are learning about in this chapter. Call
# the function, and make sure the message displays correctly.
print('### EXERCISE 8-1 ###')
def display_message():
    print('Hi everyone! In this chapter 8 of Python Crash Course, I\'m learning Functions!')

display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call
print('\n### EXERCISE 8-2 ###')
def favorite_book(title):
    print(f'One of my favorite books is {title.title()}')

favorite_book(title='the game of thrones')

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should
# print a sentence summarizing the size of the shirt and the message printed
# on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
print('\n### EXERCISE 8-3 ###')
def make_shirt(size, message):
    print(f'Making a {size.title()} T-Shirt with "{message}" printed on it.')

make_shirt('medium', 'Dunder Mifflin')
make_shirt(message='SCHRUTE FARMS - Bed & Breakfast', size='large')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a
# different message.
print('\n### EXERCISE 8-4 ###')
def make_shirt(size='large', message='I love Python'):
    print(f'Making a {size.upper()} T-Shirt with "{message}" printed on it.')

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='just play the right notes')

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
print('\n### EXERCISE 8-5 ###')
def describe_city(city, country='brazil'):
    print(f'{city.title()} is in {country.title()}.')

describe_city('guarulhos')
describe_city('salvador')
describe_city('buenos aires', 'argentina')

# 8-6. City Names: Write a function called city_country() that takes in the
# name of a city and its country. The function should return a string formatted
# like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.
print('\n### EXERCISE 8-6 ###')
def city_country(city, country):
    return f'{city.title()}, {country.title()}'

print(city_country(city='são paulo', country='brasil'))
print(city_country(city='buenos aires', country='argentina'))
print(city_country(city='salvador', country='brasil'))

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing
# different albums. Print each return value to show that the dictionaries are
# storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value
# for the number of songs, add that value to the album’s dictionary. Make at
# least one new function call that includes the number of songs on an album.
print('\n### EXERCISE 8-7 ###')
def make_album(artist_name, album_title, number_of_songs=None):
    music_album = {
        'artist': artist_name,
        'album': album_title
    }

    if number_of_songs:
        music_album['songs'] = number_of_songs

    return music_album

urnsp = make_album(artist_name='um resgate não será possível', album_title='self-titled')
tres = make_album(artist_name='hoovaranas', album_title='tres')
white_pony = make_album(artist_name='deftones', album_title='white pony')
print(urnsp)
print(tres)
print(white_pony)

urnsp['songs'] = 5
tres['songs'] = 8
white_pony['songs'] = 12
print(urnsp)
print(tres)
print(white_pony)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the
# dictionary that’s created. Be sure to include a quit value in the while loop.
print('\n### EXERCISE 8-8 ###')
while True:
    print("\nLet's make an album!") 
    print("(enter 'q' at any time to quit)") 

    QUIT = 'q'
 
    band_name = input("Band's name: ") 
    if band_name.lower() == QUIT: 
        break 
 
    album_title = input("Album title: ") 
    if album_title.lower() == QUIT: 
        break 
 
    album = make_album(artist_name=band_name, album_title=album_title) 
    print(f"\nHere is your album!\n{album}")
