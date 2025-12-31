from city_functions import get_formatted_location

# 11-1. City, Country: Write a function called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string. Run
# the test, and make sure test_city_country() passes.
def test_city_country():
    """Do cities and countries names like 'São Paulo, Brasil' work?""" 

    formatted_location = get_formatted_location('são paulo', 'brasil')
    assert formatted_location == 'São Paulo, Brasil'

# 11-2. Population: Write a second test called test_city_country_population() that verifies you
# can call your function with the values 'santiago', 'chile', and
# 'population=5000000'. Run the tests one more time, and make sure this new
# test passes
def test_city_country_population():
    """
    Do cities and countries names like 'Guarulhos, Brasil' and population like 
    1291771 work?
    """

    formatted_location = get_formatted_location('são paulo', 'brasil', 1291771)
    assert formatted_location == 'São Paulo, Brasil - population 1291771'
    