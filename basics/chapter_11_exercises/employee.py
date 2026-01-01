# 11-3. Employee: Write a class called Employee. The __init__() method
# should take in a first name, a last name, and an annual salary, and store
# each of these as attributes. Write a method called give_raise() that adds
# $5,000 to the annual salary by default but also accepts a different raise
# amount.
class Employee:
    """A simple representation of an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee with first and last names and annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Give the employee a raise."""
        self.annual_salary += raise_amount
