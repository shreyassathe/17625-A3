import grpc
import service.library_pb2
import service.library_pb2_grpc

class inventory_client:
    def __init__(self):
        self.address = "localhost"
        self.port = "50051"

    def run(self, isbn):
        url = self.address + ":" + self.port
        with grpc.insecure_channel(url) as channel:
            stub = service.library_pb2_grpc.InventoryServiceStub(channel)
            request = service.library_pb2.ISBN(isbn=isbn)
            response = stub.GetBook(request)
            return response
