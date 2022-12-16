from inventory_client import inventory_client
from get_book_titles import get_titles

import unittest.mock


class book:
    def __init__(self, isbn, name):
        self.id = isbn
        self.name = name


def new_run(arg):
    values = dict()
    values["1a"] = book("1a", "Master of Game")
    values["3c"] = book("3c", "Subtle Art")
    result = values[arg]
    return result


def test_case(client_name):
    isbn_list = ["1a", "3c"]
    result = get_titles(client_name, isbn_list)
    assert result == ["Master of Game", "Subtle Art"]
    print("Test passed")


@unittest.mock.patch("client.inventory_client.inventory_client.run")
def mock_obj(clnt):
    clnt.run = new_run
    return clnt


def mock_test():
    obj = mock_obj()
    # creating a mock client object that returns
    # the appropriate values from a dictionary is used
    test_case(obj)


def unit_test():
    ic = inventory_client()
    # actual client object is instantiated
    test_case(ic)


if __name__ == "__main__":
    unit_test()
    mock_test()
