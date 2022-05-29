# practice 8-6

from itertools import count


def city_country(city, country):
    sum = f"{city}, {country}"
    return sum

t = city_country("Beijing", "China")
print(t)