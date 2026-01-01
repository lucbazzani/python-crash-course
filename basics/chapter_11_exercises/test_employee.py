# 11-3. Employee: Write a test file for Employee with two test functions,
# test_give_default_raise() and test_give_custom_raise(). Write your tests once
# without using a fixture, and make sure they both pass. Then write a fixture
# so you don’t have to create a new employee instance in each test function.
# Run the tests again, and make sure both tests still pass.
import pytest
from employee import Employee

# First of all, testing without a fixture
# def test_give_default_raise():
#     """Test that a default raise works correctly."""

#     employee = Employee(first_name='Lucas', last_name='Bazzani', annual_salary=60000)
#     employee.give_raise()
#     assert 65000 == employee.annual_salary
    
# def test_give_custom_raise():
#     """Test that a custom raise works correctly."""

#     employee = Employee(first_name='Gon', last_name='Freecs', annual_salary=40000)
#     employee.give_raise(2000)
#     assert 42000 == employee.annual_salary

@pytest.fixture
def employee():
    """A employee that will be available to all test functions."""
    return Employee(first_name='Lucas', last_name='Bazzani', annual_salary=60000)

def test_give_default_raise(employee):
    """Test that a default raise works correctly."""
    
    initial_salary = employee.annual_salary
    employee.give_raise()
    assert employee.annual_salary == initial_salary + 5000
    
def test_give_custom_raise(employee):
    """Test that a custom raise works correctly."""
    
    initial_salary = employee.annual_salary
    raise_amount = 2000
    employee.give_raise(raise_amount)
    assert employee.annual_salary == initial_salary + raise_amount
