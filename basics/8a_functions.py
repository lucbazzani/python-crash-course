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