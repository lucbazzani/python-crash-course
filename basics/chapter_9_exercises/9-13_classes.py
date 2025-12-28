# 9-13. Dice: Make a class Die with one attribute called sides, which has a
# default value of 6. Write a method called roll_dice() that prints a random
# number between 1 and the number of sides the die has. Make a 6-sided dice
# and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import randint

class Die:
    """A simple representation of a die."""

    def __init__(self, sides=6):
        """Initialize the die with a given number of sides."""
        self.sides = sides

    def roll_die(self):
        """Simulate rolling the die and print the result."""
        print(randint(1, self.sides))


def keep_rolling_die(die, times_rolling):
    """Roll a given die a specified number of times."""
    print(f'\nRolling a {die.sides}-sided die {times_rolling} times:')
    while times_rolling > 0:    
        die.roll_die()

        times_rolling -= 1


die_1 = Die()
keep_rolling_die(die_1, 10)

die_2 = Die(10)
keep_rolling_die(die_2, 10)

die_3 = Die(20)
keep_rolling_die(die_3, 10)
