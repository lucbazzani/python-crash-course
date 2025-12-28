# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to
# win the kind of lottery you just modeled. Make a list or tuple called my_ticket.
# Write a loop that keeps pulling numbers until your ticket wins. Print a
# message reporting how many times the loop had to run to give you a
# winning ticket.
from random import sample

chars = ('A', 'B', 'C', 'D', 'E', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
my_ticket = ['0', '2', 'E', '3']
result = sample(chars, 4)
draws = 1

while result != my_ticket:
    result = sample(chars, 4)
    draws += 1

print(f'My ticket won after {draws} draws.')
