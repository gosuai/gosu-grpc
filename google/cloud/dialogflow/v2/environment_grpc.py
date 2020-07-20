# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/v2/environment.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.api.client_pb2
import google.cloud.dialogflow.v2.environment_pb2


class EnvironmentsBase(abc.ABC):

    @abc.abstractmethod
    async def ListEnvironments(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2.environment_pb2.ListEnvironmentsRequest, google.cloud.dialogflow.v2.environment_pb2.ListEnvironmentsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.v2.Environments/ListEnvironments': grpclib.const.Handler(
                self.ListEnvironments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2.environment_pb2.ListEnvironmentsRequest,
                google.cloud.dialogflow.v2.environment_pb2.ListEnvironmentsResponse,
            ),
        }


class EnvironmentsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListEnvironments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2.Environments/ListEnvironments',
            google.cloud.dialogflow.v2.environment_pb2.ListEnvironmentsRequest,
            google.cloud.dialogflow.v2.environment_pb2.ListEnvironmentsResponse,
        )
