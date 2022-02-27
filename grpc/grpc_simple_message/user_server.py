from concurrent import futures
import logging

import grpc
import user_pb2
import user_pb2_grpc

fake_users_db = {
    "taptorestart@gmail.com": {
        "id": 1,
        "email": "taptorestart@gmail.com",
        "is_active": 1,
        "is_superuser": 1
    },
}


class User(user_pb2_grpc.UserServiceServicer):

    def GetUser(self, request, context):
        email = request.email
        print(email)
        if email in fake_users_db:
            user_dict = fake_users_db[email]
            user = user_pb2.User()
            user.id = user_dict['id']
            user.email = user_dict['email']
            user.is_active = user_dict['is_active']
            user.is_superuser = user_dict['is_superuser']
            return user


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(User(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
