import grpc
import user_pb2
import user_pb2_grpc
import mysql.connector

SERVER_ADDRESS = '0.0.0.0'
PORT = 8080

class ExampleServiceClient(object):
    def __init__(self):
        """Initializer. 
           Creates a gRPC channel for connecting to the server.
           Adds the channel to the generated client stub.
        Arguments:
            None.
        Returns:
            None.
        """
        self.channel = grpc.insecure_channel(f'{SERVER_ADDRESS}:{PORT}')
        self.stub = user_pb2_grpc.ExampleServiceStub(self.channel)
    
    def get_user(self, name, display_name,email):
        """Gets a user.
        Arguments:
            name: The resource name of a user.
        
        Returns:
            None; outputs to the terminal.
        """
        request = user_pb2.GetUserRequest(
            name = name,
            display_name = display_name,
            email = email
        )
        try:
            response = self.stub.GetUser(request)
            print('User fetched.')
            print(response)
        except grpc.RpcError as err:
            print(err.details()) #pylint: disable=no-member
            print('{}, {}'.format(err.code().name, err.code().value)) #pylint: disable=no-member

    def CreateUserRequest(self,name,display_name,email):
        
        request=user_pb2.CreateUserRequest(
            name=name,
            display_name=display_name,
            email=email
        )
        try:
            response=self.stub.CreateUser(request)
            print('User created.')
            print(response)          
        except grpc.RpcError as err:
            print(err.details())
