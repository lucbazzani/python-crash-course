# 6-1. Person: Use a dictionary to store information about a person you
# know. Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
print('### EXERCISE 6-1 ###')
person = {
    'first_name': 'ester',
    'last_name': 'bazzani',
    'age': 23,
    'city': 'guarulhos - sp'
}

print(f'My sister is called {person.get("first_name").title()} {person.get("last_name").title()}. She is {person.get('age')} and lives in {person.get("city").title()}.')

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite
# numbers. Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in
# your dictionary. Print each person’s name and their favorite number. For
# even more fun, poll a few friends and get some actual data for your
# program
print('\n### EXERCISE 6-2 ###')
favorite_numbers = {
    'lucas': 3,
    'ester': 9,
    'gon': 1,
    'kite': 7,
    'meruem': 3
}
print(f'The Lucas\'s favorite number is {favorite_numbers.get('lucas')}!')
print(f'The Ester\'s favorite number is {favorite_numbers.get('ester')}!')
print(f'The Gon\'s favorite number is {favorite_numbers.get('gon')}!')
print(f'The Kite\'s favorite number is {favorite_numbers.get('kite')}!')
print(f'The Meruem\'s favorite number is {favorite_numbers.get('meruem')}!')

# 6-3. Glossary: A Python dictionary can be used to model an actual
# dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# Print each word and its meaning as neatly formatted output. You might print
# the word followed by a colon and then its meaning, or print the word on one
# line and then print its meaning indented on a second line. Use the newline
# character (\n) to insert a blank line between each word-meaning pair in your
# output.
print('\n### EXERCISE 6-3 ###')
glossary = {
    'statement': 'something that someone says or writes officially, or an action done to express an opinion',
    'forth': '(from a place) out or away, or (from a point in time) forward',
    'colon': 'the symbol : used in writing, especially to introduce a list of things or a sentence or phrase taken from somewhere else',
    'poll': 'a study in which people are asked for their opinions about a subject or person',
    'evaluate': 'to judge or calculate the quality, importance, amount, or value of something'
}

print(f'STATEMENT:\n\t{glossary.get('statement')}.')
print(f'\nFORTH:\n\t{glossary.get('forth')}.')
print(f'\nCOLON:\n\t{glossary.get('colon')}.')
print(f'\nPOLL:\n\t{glossary.get('poll')}.')
print(f'\nEVALUATE:\n\t{glossary.get('evaluate')}.')

# 6-4. Glossary 2: Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 99) by replacing your series of
# print() calls with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.
print('\n### EXERCISE 6-4 ###')
glossary = {
    'statement': 'something that someone says or writes officially, or an action done to express an opinion',
    'forth': '(from a place) out or away, or (from a point in time) forward',
    'colon': 'the symbol : used in writing, especially to introduce a list of things or a sentence or phrase taken from somewhere else',
    'poll': 'a study in which people are asked for their opinions about a subject or person',
    'evaluate': 'to judge or calculate the quality, importance, amount, or value of something'
}

for k, v in glossary.items():
    print(f'{k.upper()}:\n\t{v}.\n')

glossary['comma'] = 'the symbol , used in writing to separate parts of a sentence showing a slight pause, or to separate the single things in a list'
glossary['topping'] = 'a substance, especially a sauce or pieces of food, that is put on top of other food to give extra flavour and to make it look attractive'
glossary['prompt'] = 'to give an instruction to an artificial intelligence (= a computer system or machine that has some of the qualities that a human brain has, such as the ability to interpret and produce language in a way that seems human, recognize or create images, solve problems, and learn from data supplied to it) using natural language rather than computer language'
glossary['ensure'] = 'to make something certain to happen'
glossary['likewise'] = 'in the same way'

for k, v in glossary.items():
    print(f'{k.upper()}:\n\t{v}.\n')

# 6-5. Rivers: Make a dictionary containing three major rivers and the
# country each river runs through. One key-value pair might be 'nile': 'egypt'.
# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.
print('\n### EXERCISE 6-4 ###')
rivers = {
    'amazonas': 'brazil',
    'nile': 'egypt',
    'yangtzé': 'china'
}

for k, v in rivers.items():
    print(f'The {k.title()} runs through {v.title()}')

print('\n### RIVERS ###')
for river in rivers.keys():
    print(river.title())

print('\n### COUNTRIES ###')
for country in set(rivers.values()): 
    print(country.title())

# 6-6. Polling: Use the code in favorite_languages.py (page 96).
# Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already
# taken the poll, print a message thanking them for responding. If they have
# not yet taken the poll, print a message inviting them to take the poll.
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust', 
    'phil': 'python', 
    }
 
print("The following languages have been mentioned:") 
for language in favorite_languages.values(): 
    print(language.title())

names = ['jen', 'phil', 'joão', 'karina']

print()
for person in names:
    if person in favorite_languages.keys():
        print(f'Thank you, {person.title()} for responding the poll!')
    else:
        print(f'{person.title()}, please take the poll.')

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
print('\n### EXERCISE 6-7 ###')
person_1 = {
    'first_name': 'ester',
    'last_name': 'bazzani',
    'age': 23,
    'city': 'guarulhos - sp'
}
person_2 = {
    'first_name': 'raí',
    'last_name': 'bazzani',
    'age': 0.25,
    'city': 'guarulhos - sp'
}
person_3 = {
    'first_name': 'henrique',
    'last_name': 'topfstedt',
    'age': 29,
    'city': 'katowice - poland'
}
people = [person_1, person_2, person_3]

for person in people:
    full_name = person.get('first_name') + ' ' + person.get('last_name')
    age = person.get('age')
    city = person.get('city')
    print(f'\n{full_name.title()} is {age} years old and lives in {city.title()}.')

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page
# 98) so each person can have more than one favorite number. Then print
# each person’s name along with their favorite numbers.
print('\n### EXERCISE 6-10 ###')
favorite_numbers = {
    'lucas': [3],
    'ester': [9, 10],
    'gon': [1],
    'kite': [7, 13],
    'meruem': [1, 3]
}
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f'\nThe {name.title()}\'s favorite number is {numbers[0]}')
    else:
        print(f"\n{name.title()}'s favorite numbers are:") 
        
        for number in numbers: 
            print(f"\t{number}")
