# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a
# module. Make a separate file that imports Restaurant. Make a Restaurant
# instance, and call one of Restaurant’s methods to show that the import
# statement is working properly.
from modules_exercises_chapter_9.restaurant_class import Restaurant

restaurant = Restaurant('Bazzani', 'Brazilian food')
restaurant.open_restaurant()
