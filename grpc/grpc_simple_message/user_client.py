from __future__ import print_function

import logging

import grpc
import user_pb2
import user_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        user = stub.GetUser(user_pb2.UserRequest(email='taptorestart@gmail.com'))
    print(f'user.id: {user.id}')
    print(f'user.email: {user.email}')
    print(f'user.is_active: {user.is_active}')
    print(f'user.is_superuser: {user.is_superuser}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
