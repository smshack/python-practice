# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import RelayServerRPC_pb2 as RelayServerRPC__pb2


class RelayServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.STT = channel.stream_unary(
                '/RelayServer.RelayServer/STT',
                request_serializer=RelayServerRPC__pb2.reqSpeech.SerializeToString,
                response_deserializer=RelayServerRPC__pb2.resText.FromString,
                )


class RelayServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def STT(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RelayServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'STT': grpc.stream_unary_rpc_method_handler(
                    servicer.STT,
                    request_deserializer=RelayServerRPC__pb2.reqSpeech.FromString,
                    response_serializer=RelayServerRPC__pb2.resText.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RelayServer.RelayServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RelayServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def STT(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/RelayServer.RelayServer/STT',
            RelayServerRPC__pb2.reqSpeech.SerializeToString,
            RelayServerRPC__pb2.resText.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)