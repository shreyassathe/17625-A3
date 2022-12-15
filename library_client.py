import grpc
import service.library_pb2
import service.library_pb2_grpc
import time

def run():
    while(True):
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = service.library_pb2_grpc.InventoryServiceStub(channel)
            print("1. Create book")
            print("2. fetch book with isbn")
            rpc_call = input("Choose action: ")

            if rpc_call == "1":
                _id = input("id: ")
                name = input("name: ")
                author = input("author: ")
                year = int(input("year: "))
                genre = int(input("Genre: "))

                isbn = service.library_pb2.ISBN(isbn=_id)
                request = service.library_pb2.Book(id=isbn, name=name, author=author, year=year)
                request.genre = genre;
                response = stub.CreateBook(request)
                print(response)

            elif rpc_call == "2":
                id = input("id: ")
                request = service.library_pb2.ISBN(isbn=id)
                response = stub.GetBook(request)
                print(response)

            else:
                break


if __name__ == "__main__":
    run()
