from .user_class import User

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
