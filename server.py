from concurrent import futures
import logging

import grpc

import hellonerd_pb2
import hellonerd_pb2_grpc


class HelloNerd(hellonerd_pb2_grpc.HelloNerd):

    def SayHello(self, request, context):
        return hellonerd_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hellonerd_pb2_grpc.add_HelloNerdServicer_to_server(HelloNerd(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
