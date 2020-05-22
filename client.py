from __future__ import print_function
import logging

import grpc

import hellonerd_pb2
import hellonerd_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50055') as channel:
        stub = hellonerd_pb2_grpc.HelloNerdStub(channel)
        response = stub.SayHello(hellonerd_pb2.HelloRequest(name='test'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()