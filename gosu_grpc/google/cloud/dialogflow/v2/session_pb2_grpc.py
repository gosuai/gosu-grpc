# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from gosu_grpc.google.cloud.dialogflow.v2 import session_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2


class SessionsStub(object):
    """A session represents an interaction with a user. You retrieve user input
    and pass it to the [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
    [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) method to determine
    user intent and respond.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DetectIntent = channel.unary_unary(
                '/google.cloud.dialogflow.v2.Sessions/DetectIntent',
                request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.DetectIntentRequest.SerializeToString,
                response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.DetectIntentResponse.FromString,
                )
        self.StreamingDetectIntent = channel.stream_stream(
                '/google.cloud.dialogflow.v2.Sessions/StreamingDetectIntent',
                request_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.StreamingDetectIntentRequest.SerializeToString,
                response_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.StreamingDetectIntentResponse.FromString,
                )


class SessionsServicer(object):
    """A session represents an interaction with a user. You retrieve user input
    and pass it to the [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
    [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) method to determine
    user intent and respond.
    """

    def DetectIntent(self, request, context):
        """Processes a natural language query and returns structured, actionable data
        as a result. This method is not idempotent, because it may cause contexts
        and session entity types to be updated, which in turn might affect
        results of future queries.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingDetectIntent(self, request_iterator, context):
        """Processes a natural language query in audio format in a streaming fashion
        and returns structured, actionable data as a result. This method is only
        available via the gRPC API (not REST).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SessionsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DetectIntent': grpc.unary_unary_rpc_method_handler(
                    servicer.DetectIntent,
                    request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.DetectIntentRequest.FromString,
                    response_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.DetectIntentResponse.SerializeToString,
            ),
            'StreamingDetectIntent': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingDetectIntent,
                    request_deserializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.StreamingDetectIntentRequest.FromString,
                    response_serializer=google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.StreamingDetectIntentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.cloud.dialogflow.v2.Sessions', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Sessions(object):
    """A session represents an interaction with a user. You retrieve user input
    and pass it to the [DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent] (or
    [StreamingDetectIntent][google.cloud.dialogflow.v2.Sessions.StreamingDetectIntent]) method to determine
    user intent and respond.
    """

    @staticmethod
    def DetectIntent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.dialogflow.v2.Sessions/DetectIntent',
            google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.DetectIntentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.DetectIntentResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingDetectIntent(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/google.cloud.dialogflow.v2.Sessions/StreamingDetectIntent',
            google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.StreamingDetectIntentRequest.SerializeToString,
            google_dot_cloud_dot_dialogflow_dot_v2_dot_session__pb2.StreamingDetectIntentResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
