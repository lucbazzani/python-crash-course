# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called
# increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of
# login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and then call reset_login_attempts(). Print
# login_attempts again to make sure it was reset to 0.
class User:
    """A simple representation of an user model."""

    def __init__(self, first_name, last_name, id, email, password):
        """Initialize first_name and last_name attributes.""" 
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.email = email
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Print a statement describing the user."""
        print(f'User: {self.first_name} {self.last_name}\nId: {self.id}\nEmail: {self.email}')

    def greet_user(self):
        """Print a statement greeting the user."""
        print(f'\nHello, {self.first_name} {self.last_name}! Welcome to our platform!\n')

    def increment_login_attempts(self):
        """Increments the value of login_attempts by 1"""
        print('User has logged in!')
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts to 0."""
        print('The user login attempt count was reset.')
        self.login_attempts = 0

    def print_login_attempts(self):
        """Prints the number of login attempts."""     
        logged_in_times = ''
        if self.login_attempts == 1:
            logged_in_times = f'{self.login_attempts} time'
        else:
            logged_in_times = f'{self.login_attempts} times'

        print(f'User has logged in {logged_in_times}.\n')


user = User('Lucas', 'Bazzani', 1, 'lucas@email.com', '123456')
for i in range(3):
    user.increment_login_attempts()
    user.print_login_attempts()

user.reset_login_attempts()
user.print_login_attempts()
