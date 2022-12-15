generate:
	python3 -m grpc_tools.protoc --proto_path=protos --python_out=service --pyi_out=service --grpc_python_out=service library.proto