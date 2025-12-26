# 9-4. Number Served: Start with your program from Exercise 9-1 (page
# 162). Add an attribute called number_served with a default value of 0. Create
# an instance called restaurant from this class. Print the number of customers
# the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment the
# number of customers who’ve been served. Call this method with any
# number you like that could represent how many customers were served in,
# say, a day of business.
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
        return f'The {restaurant.restaurant_name}\'s restaurant had been served {restaurant.number_served} people.'


restaurant = Restaurant('Bazzani', 'Brazilian food')
print(restaurant.get_number_served())

restaurant.number_served = 33
print(restaurant.get_number_served())

restaurant.set_number_served(28)
print(restaurant.get_number_served())

restaurant.increment_number_served(16)
print(restaurant.get_number_served())
