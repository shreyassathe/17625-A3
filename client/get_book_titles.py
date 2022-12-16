
from inventory_client import inventory_client as ic

def get_titles(client_object, isbn_list):
    book_list = list()

    for id in isbn_list:
        response = client_object.run(id)
        book_list.append(response.name)
    return book_list


if __name__ == "__main__":
    client_object = ic()
    isbn_list = ["1a", "3c"]
    out = get_titles(client_object, isbn_list)
    for t in out:
        print(t)



