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

print(f'STATEMENT:\n    {glossary.get('statement')}.')
print(f'\nFORTH:\n    {glossary.get('forth')}.')
print(f'\nCOLON:\n    {glossary.get('colon')}.')
print(f'\nPOLL:\n    {glossary.get('poll')}.')
print(f'\nEVALUATE:\n    {glossary.get('evaluate')}.')