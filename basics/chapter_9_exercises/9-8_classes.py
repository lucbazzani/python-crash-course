# 9-8. Privileges: Write a separate Privileges class. The class should have
# one attribute, privileges, that stores a list of strings as described in Exercise
# 9-7. Move the show_privileges() method to this class. Make a Privileges
# instance as an attribute in the Admin class. Create a new instance of Admin
# and use your method to show its privileges.
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
        """Increments the value of login_attempts by 1."""
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


class Admin(User):
    """Represent aspects of an Administrator user."""

    def __init__(self, first_name, last_name, id, email, password, privileges): 
        """  
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an administrator user. 
        """
        super().__init__(first_name, last_name, id, email, password) 
        self.privileges = privileges    


class Privileges:
    """A simple representation of user's privileges."""

    def __init__(self, privileges):
        """Initialize privileges attributes.""" 
        self.privileges = privileges

    def show_privileges(self):
        """Display the user's privileges in an organized way."""
        print(f'This user has the following privileges:')
        for privilege in self.privileges:
            print(f'\t- {privilege.capitalize()}')


privileges = Privileges(['can edit post', 'can delete post', 'can ban other users'])
admin = Admin('Lucas', 'Bazzani', 1, 'lucas@email.com', '123456', privileges)

admin.privileges.show_privileges()
