# practice 8-4

from pydoc import describe


def describe_city(city_name='Beijing', city_from='China'):
    print(f"{city_name} is in {city_from}.")

describe_city()
describe_city("Shanghai")
describe_city("Tokyo", "Japan")