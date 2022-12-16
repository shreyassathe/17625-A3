from concurrent import futures
import time

import grpc
import library_pb2
import library_pb2_grpc


class Book:
    def __init__(self, isbn, name, author, genre, year):
        self.id = isbn
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year


BookDictionary = dict();

BookDictionary["1a"] = Book("1a", "Master of Game", "Sidney Sheldon", 1, 2000)
BookDictionary["2b"] = Book("2b", "Harry Potter", "JK Rowling", 2, 2000)
BookDictionary["3c"] = Book("3c", "Subtle Art", "Charles", 3, 2010)
BookDictionary["4q"] = Book("4q", "Concepts of Physics", "HC Verma", 3, 2005)

def add_book(isbn, name, author, genre, year):
    BookDictionary[isbn] = Book(isbn, name, author, genre, year)

def get_book(isbn):
    if isbn not in BookDictionary.keys():
        return Book("", "", "", 0, 0)
    return BookDictionary[isbn]

def print_book_dict():
    for id in BookDictionary.keys():
        obj = BookDictionary[id]
        print(obj.id)
        print(obj.name)
        print(obj.genre)
        print(obj.author)
        print(obj.year)
        print("")


class LibraryServicer(library_pb2_grpc.InventoryServiceServicer):
    def CreateBook(self, request, context):
        add_book(request.id.isbn, request.name, request.author, request.genre, request.year)
        print("create book called")
        print_book_dict()
        reply = library_pb2.Empty()
        return reply

    def GetBook(self, request, context):
        result = get_book(request.isbn)
        isbn = library_pb2.ISBN(isbn=result.id)
        book = library_pb2.Book(id=isbn)
        book.genre = result.genre
        book.name = result.name
        book.year = result.year
        book.author = result.author
        return book;


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_InventoryServiceServicer_to_server(LibraryServicer(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    print("server is running")
    print_book_dict()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()


