# 7-1. Rental Car: Write a program that asks the user what kind of rental car
# they would like. Print a message about that car, such as "Let me see if I can
# find you a Subaru."
# print('### EXERCISE 6-1 ###')
# car = input("What kind of rental car would you like?\n")
# print(f'\nLet me see if I can find you a {car.title()}.')

# 7-2. Restaurant Seating: Write a program that asks the user how many
# people are in their dinner group. If the answer is more than eight, print a
# message saying they’ll have to wait for a table. Otherwise, report that their
# table is ready.
print('\n### EXERCISE 6-2 ###')
number_of_people = input('How many people are in your dinner group?\n')
number_of_people = int(number_of_people)

if number_of_people > 8:
    print('\nYou\'ll need to wait until we have a table ready for you.')
else:
    print('\nYour table is ready!')

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether
# the number is a multiple of 10 or not.
print('\n### EXERCISE 6-3 ###')
number = input('Please, enter a number: ')
number = int(number)

if number % 10 == 0:
    print(f'\n{number} is multiple of 10.')
else:
    print(f'\n{number} is not multiple of 10.')
