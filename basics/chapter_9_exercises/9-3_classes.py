# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that prints a
# summary of the user’s information. Make another method called greet_user()
# that prints a personalized greeting to the user.
# Create several instances representing different users, and call both
# methods for each user.
class User:
    """A simple representation of an user model."""

    def __init__(self, first_name, last_name, id, email, password):
        """Initialize first_name and last_name attributes.""" 
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.email = email
        self.password = password

    def describe_user(self):
        """Print a statement describing the user."""
        print(f'User: {self.first_name} {self.last_name}\nId: {self.id}\nEmail: {self.email}')

    def greet_user(self):
        """Print a statement greeting the user."""
        print(f'\nHello, {self.first_name} {self.last_name}! Welcome to our platform!\n')


user_1 = User('Lucas', 'Bazzani', 1, 'lucas@email.com', '123456')
user_2 = User('Ester', 'Bazzani', 2, 'ester@email.com', '7890abc')
user_3 = User('Raí', 'Bazzani', 4, 'rai@email.com', 'def12345')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
