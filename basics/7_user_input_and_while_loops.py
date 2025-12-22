# 7-1. Rental Car: Write a program that asks the user what kind of rental car
# they would like. Print a message about that car, such as "Let me see if I can
# find you a Subaru."
print('### EXERCISE 7-1 ###')
car = input("What kind of rental car would you like?\n")
print(f'\nLet me see if I can find you a {car.title()}.')

# 7-2. Restaurant Seating: Write a program that asks the user how many
# people are in their dinner group. If the answer is more than eight, print a
# message saying they’ll have to wait for a table. Otherwise, report that their
# table is ready.
print('\n### EXERCISE 7-2 ###')
number_of_people = input('How many people are in your dinner group?\n')
number_of_people = int(number_of_people)

if number_of_people > 8:
    print('\nYou\'ll need to wait until we have a table ready for you.')
else:
    print('\nYour table is ready!')

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether
# the number is a multiple of 10 or not.
print('\n### EXERCISE 7-3 ###')
number = input('Please, enter a number: ')
number = int(number)

if number % 10 == 0:
    print(f'\n{number} is multiple of 10.')
else:
    print(f'\n{number} is not multiple of 10.')

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
print('\n### EXERCISE 7-4 ###')
prompt = '\nEnter the pizza toppings you would like to order (one per line, or enter "quit" to finish): '
active = True

while active:
    message = input(prompt)

    if message.lower() == 'quit':
        active = False
    else:
        print(f'The {message.title()} topping has been added to your order!')

# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that
# do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.
print('\n### EXERCISE 7-6 ###')

# conditional test
prompt = '\nEnter the pizza toppings you would like to order (one per line, or enter "quit" to finish): '
message = ''

while message.lower() != 'quit':
    message = input(prompt)

    if message.lower() != 'quit':
        print(f'The {message.title()} topping has been added to your order!')

# active variable
prompt = '\nEnter the pizza toppings you would like to order (one per line, or enter "quit" to finish): '
active = True

while active:
    message = input(prompt)

    if message.lower() == 'quit':
        active = False
    else:
        print(f'The {message.title()} topping has been added to your order!')

# break statement
prompt = '\nEnter the pizza toppings you would like to order (one per line, or enter "quit" to finish): '

while True:
    message = input(prompt)

    if message.lower() == 'quit':
        break
    else:
        print(f'The {message.title()} topping has been added to your order!')
