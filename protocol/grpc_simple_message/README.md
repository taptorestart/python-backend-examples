# gRPC Simple Message Example
Reference: [gRPC Quickstart](https://grpc.io/docs/languages/python/quickstart/)

## Test Environments
- Python v3.8.2
- MacOS v12.2.1

## Install
```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Make proto file user.proto
```
syntax = "proto3";

package grpc;

service UserService {
  rpc GetUser (UserRequest) returns (User) {}
}

message User {
  int32 id = 1;
  string email = 2;
  int32 is_active = 3;
  int32 is_superuser = 4;
}

message UserRequest {
  string email = 1;
}
```

###Make pb2 files for user.proto

Format
```shell
python -m grpc_tools.protoc -I {proto_file_directory} --python_out={python_output_file_directory} --grpc_python_out={grpc_python_output_file_directory} {proto_file_path}
```

Example for user.proto
```shell
python -m grpc_tools.protoc -I ./protos --python_out=. --grpc_python_out=.  ./protos/user.proto
```

###Run server
```shell
$ python user_server.py
```
Result
```
taptorestart@gmail.com
```

###Run client
From another terminal, run the client
```shell
$ python user_client.py
```
Result
```
user.id: 1
user.email: taptorestart@gmail.com
user.is_active: 1
user.is_superuser: 1
```
