# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create
# three different instances from the class, and call describe_restaurant() for
# each instance.
class Restaurant:
    """A simple representation of a model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes.""" 
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print a statement showing the restaurant's description."""
        print(f'{self.restaurant_name} {self.cuisine_type}')

    def open_restaurant(self):
        """Print a statement indicating that the restaurant is open."""
        print(f'{self.restaurant_name} is now open!')


restaurant_1 = Restaurant('Bazzani', 'Brazilian food')
restaurant_2 = Restaurant('Rinpoche', 'Tibetan food')
restaurant_3 = Restaurant('Héctor Rivera', 'Mexican food')

restaurant_1.describe_restaurant()
restaurant_3.describe_restaurant()
restaurant_2.describe_restaurant()
