# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each
# pizza.
# Modify your for loop to print a sentence using the name of the pizza, instead
# of printing just the name of the pizza. For each pizza, you should have one
# line of output containing a simple statement like I like pepperoni pizza.
# Add a line at the end of your program, outside the for loop, that states how
# much you like pizza. The output should consist of three or more lines about
# the kinds of pizza you like and then an additional sentence, such as I really
# love pizza!
print('### EXERCISE 4-1 ###')
pizzas = ['veggie','margherita','neapolitan','mushroom']
for pizza in pizzas:
    print(f"{pizza.title()} pizza is tasty.")

print("I love pizza for dinner!")

# 4-2. Animals: Think of at least three different animals that have a common
# characteristic. Store the names of these animals in a list, and then use a for
# loop to print out the name of each animal.
# Modify your program to print a statement about each animal, such as A dog
# would make a great pet.
# Add a line at the end of your program, stating what these animals have in
# common. You could print a sentence, such as Any of these animals would
# make a great pet!
print('\n### EXERCISE 4-2 ###')
animals = ['sabiá', 'bem-te-vi', 'harpia', 'pavão']
for animal in animals:
    print(animal.title())

for animal in animals:
    print(f"{animal.title()} is a wild bird.")

print("All of these animals are brazilian birds.")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to
# 20, inclusive.
print('\n### EXERCISE 4-3 ###')
for number in range(1, 21):
    print(number)

# 4-4. One Million: Make a list of the numbers from one to one million, and
# then use a for loop to print the numbers. (If the output is taking too long,
# stop it by pressing CTRL-C or by closing the output window.)
print('\n### EXERCISE 4-4 ###')
numbers = list(range(1, 1000001))
for i in numbers:
    print(i)

# 4-5. Summing a Million: Make a list of the numbers from one to one
# million, and then use min() and max() to make sure your list actually starts at
# one and ends at one million. Also, use the sum() function to see how quickly
# Python can add a million numbers.
print('\n### EXERCISE 4-5 ###')
one_to_one_million = list(range(1, 1000001))
print(f'min: {min(one_to_one_million)}')
print(f'max: {max(one_to_one_million)}')
print(f'sum: {sum(one_to_one_million)}')

# 4-6. Odd Numbers: Use the third argument of the range() function to make
# a list of the odd numbers from 1 to 20. Use a for loop to print each number.
print('\n### EXERCISE 4-6 ###')
odd_numbers = list(range(1, 20, 2))
for odd in odd_numbers:
    print(odd)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to
# print the numbers in your list
print('\n### EXERCISE 4-7 ###')
multiples_of_three = list(range(3, 31, 3))
for multiple in multiples_of_three:
    print(multiple)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of
# the first 10 cubes.
print('\n### EXERCISE 4-9 ###')
cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
