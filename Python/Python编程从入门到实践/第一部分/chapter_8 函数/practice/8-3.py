# partice 8-3

from cgi import print_arguments


def make_shirt(size, text):
    print(f"The size of T-shirt is {size}")
    print(f"There are '{text}' print on it")

make_shirt("XL", "PYTHON")