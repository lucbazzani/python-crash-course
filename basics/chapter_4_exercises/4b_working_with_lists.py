# 4-10. Slices: Using one of the programs you wrote in this chapter, add
# several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:. Then use a
# slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Then use a slice to
# print the last three items in the list.
print('### EXERCISE 4-10 ###')
odd_numbers = list(range(1, 20, 2))
for odd in odd_numbers:
    print(odd)

print(f'The first three items in the list are: {odd_numbers[:3]}')
print(f'Three items from the middle of the list are: {odd_numbers[3:6]}')
print(f'The last three items in the list are: {odd_numbers[-3:]}')

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do
# the following:
# Add a new pizza to the original list.
# Add a different pizza to the list friend_pizzas.
# Prove that you have two separate lists. Print the message My favorite pizzas
# are:, and then use a for loop to print the first list. Print the message My
# friend’s favorite pizzas are:, and then use a for loop to print the second list.
# Make sure each new pizza is stored in the appropriate list.
print('\n### EXERCISE 4-11 ###')
pizzas = ['veggie','margherita','neapolitan','mushroom']
for pizza in pizzas:
    print(f"{pizza.title()} pizza is tasty.")

print("I love pizza for dinner!")

friend_pizzas = pizzas[:]

pizzas.append('mozzarella')

friend_pizzas.append('boscaiola')

print('\nMy favorite pizzas are:')
for my_pizza in pizzas:
    print(my_pizza)

print('\nMy friend\'s favorite pizzas are:')
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of
# five simple foods, and store them in a tuple.
# Use a for loop to print each food the restaurant offers.
# Try to modify one of the items, and make sure that Python rejects the
# change.
# The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.
print('\n### EXERCISE 4-13 ###')
menu = ('rice', 'salad', 'eggs', 'spaghetti', 'coxinha')
# menu[0] = 'sandwich'
menu = ('rice', 'beans', 'eggs', 'sandwich', 'coxinha')

for item in menu:
    print(item)