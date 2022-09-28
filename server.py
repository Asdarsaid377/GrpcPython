from concurrent import futures
import email
import time
import grpc
import user_pb2
import user_pb2_grpc
import mysql.connector
# Inherit from example_pb2_grpc.ExampleServiceServicer
# ExampleServiceServicer is the server-side artifact.
class ExampleServiceServicer(user_pb2_grpc.ExampleServiceServicer): 
    def GetUser(self, request, context):
        """Gets a user.
           gRPC calls this method when clients call the GetUser rpc (method).
        Arguments:
            request (GetUserRequest): The incoming request.
            context: The gRPC connection context.
        Returns:
            user (User): A user.
        """
        name = request.name
        display_name=request.display_name
        email = request.email
        user = user_pb2.User(
            name=name,
            display_name=display_name,
            email=email
        )
        print(user)
        return user

    def CreateUser(self, request, context):
        """Creates a user.
           gRPC calls this method when clients call the CreateUser rpc (method).
        Arguments:
            request (CreateUserRequest): The incoming request.
            context: The gRPC connection context.
        Returns:
            user (User): A user.
        """
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="belajargrpc"
        )
        cursor=db.cursor()
        sql="SELECT*FROM users"
        cursor.execute(sql)
        result=cursor.fetchall()
        for x in result:
            print(x)
        user = user_pb2.User(
            name=request.name,
            display_name=request.display_name,
            email=request.email,
        )
        return user


if __name__ == '__main__':
    # Run a gRPC server with one thread.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Adds the servicer class to the server.
    user_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    server.add_insecure_port('0.0.0.0:8080')
    server.start()
    print('API server started. Listening at 0.0.0.0:8080.')
    while True:
        time.sleep(60)
