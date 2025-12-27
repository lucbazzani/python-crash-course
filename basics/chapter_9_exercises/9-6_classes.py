# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand that inherits from the Restaurant class you
# wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version
# of the class will work; just pick the one you like better. Add an attribute
# called flavors that stores a list of ice cream flavors. Write a method that
# displays these flavors. Create an instance of IceCreamStand, and call this
# method.
class Restaurant:
    """A simple representation of a restaurant model."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes.""" 
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print a statement showing the restaurant's description."""
        print(f'{self.restaurant_name} {self.cuisine_type}')

    def open_restaurant(self):
        """Print a statement indicating that the restaurant is open."""
        print(f'{self.restaurant_name} is now open!')

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, customers_served):
        """Increment the number of customers who have been served."""
        self.number_served += customers_served

    def get_number_served(self):
        """Return a string summarizing the number of customers served."""
        return f'The {self.restaurant_name}\'s restaurant had been served {self.number_served} people.'


class IceCreamStand(Restaurant):
    """Represent aspects of an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, flavors): 
        """  
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an ice cream stand. 
        """
        super().__init__(restaurant_name, cuisine_type) 
        self.flavors = flavors

    def print_flavors(self):
        """Print a list of the ice cream stand's flavors."""
        print(f'Here is the {self.restaurant_name} ice cream flavor list:')
        for flavor in self.flavors:
            print(f'\t- {flavor.title()}')


flavors = ['vanilla', 'chocolate', 'strawberry', 'jack fruit', 'mango']
ice_cream_stand = IceCreamStand('Ice Kiss', 'Ice Cream Stand', flavors)

ice_cream_stand.print_flavors()
