# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/translate/v3/translation_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.longrunning.operations_pb2
import google.protobuf.timestamp_pb2
import google.cloud.translate.v3.translation_service_pb2


class TranslationServiceBase(abc.ABC):

    @abc.abstractmethod
    async def TranslateText(self, stream: 'grpclib.server.Stream[google.cloud.translate.v3.translation_service_pb2.TranslateTextRequest, google.cloud.translate.v3.translation_service_pb2.TranslateTextResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DetectLanguage(self, stream: 'grpclib.server.Stream[google.cloud.translate.v3.translation_service_pb2.DetectLanguageRequest, google.cloud.translate.v3.translation_service_pb2.DetectLanguageResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSupportedLanguages(self, stream: 'grpclib.server.Stream[google.cloud.translate.v3.translation_service_pb2.GetSupportedLanguagesRequest, google.cloud.translate.v3.translation_service_pb2.SupportedLanguages]') -> None:
        pass

    @abc.abstractmethod
    async def BatchTranslateText(self, stream: 'grpclib.server.Stream[google.cloud.translate.v3.translation_service_pb2.BatchTranslateTextRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateGlossary(self, stream: 'grpclib.server.Stream[google.cloud.translate.v3.translation_service_pb2.CreateGlossaryRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListGlossaries(self, stream: 'grpclib.server.Stream[google.cloud.translate.v3.translation_service_pb2.ListGlossariesRequest, google.cloud.translate.v3.translation_service_pb2.ListGlossariesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGlossary(self, stream: 'grpclib.server.Stream[google.cloud.translate.v3.translation_service_pb2.GetGlossaryRequest, google.cloud.translate.v3.translation_service_pb2.Glossary]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteGlossary(self, stream: 'grpclib.server.Stream[google.cloud.translate.v3.translation_service_pb2.DeleteGlossaryRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.translation.v3.TranslationService/TranslateText': grpclib.const.Handler(
                self.TranslateText,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.translate.v3.translation_service_pb2.TranslateTextRequest,
                google.cloud.translate.v3.translation_service_pb2.TranslateTextResponse,
            ),
            '/google.cloud.translation.v3.TranslationService/DetectLanguage': grpclib.const.Handler(
                self.DetectLanguage,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.translate.v3.translation_service_pb2.DetectLanguageRequest,
                google.cloud.translate.v3.translation_service_pb2.DetectLanguageResponse,
            ),
            '/google.cloud.translation.v3.TranslationService/GetSupportedLanguages': grpclib.const.Handler(
                self.GetSupportedLanguages,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.translate.v3.translation_service_pb2.GetSupportedLanguagesRequest,
                google.cloud.translate.v3.translation_service_pb2.SupportedLanguages,
            ),
            '/google.cloud.translation.v3.TranslationService/BatchTranslateText': grpclib.const.Handler(
                self.BatchTranslateText,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.translate.v3.translation_service_pb2.BatchTranslateTextRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.translation.v3.TranslationService/CreateGlossary': grpclib.const.Handler(
                self.CreateGlossary,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.translate.v3.translation_service_pb2.CreateGlossaryRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.translation.v3.TranslationService/ListGlossaries': grpclib.const.Handler(
                self.ListGlossaries,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.translate.v3.translation_service_pb2.ListGlossariesRequest,
                google.cloud.translate.v3.translation_service_pb2.ListGlossariesResponse,
            ),
            '/google.cloud.translation.v3.TranslationService/GetGlossary': grpclib.const.Handler(
                self.GetGlossary,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.translate.v3.translation_service_pb2.GetGlossaryRequest,
                google.cloud.translate.v3.translation_service_pb2.Glossary,
            ),
            '/google.cloud.translation.v3.TranslationService/DeleteGlossary': grpclib.const.Handler(
                self.DeleteGlossary,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.translate.v3.translation_service_pb2.DeleteGlossaryRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class TranslationServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.TranslateText = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.translation.v3.TranslationService/TranslateText',
            google.cloud.translate.v3.translation_service_pb2.TranslateTextRequest,
            google.cloud.translate.v3.translation_service_pb2.TranslateTextResponse,
        )
        self.DetectLanguage = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.translation.v3.TranslationService/DetectLanguage',
            google.cloud.translate.v3.translation_service_pb2.DetectLanguageRequest,
            google.cloud.translate.v3.translation_service_pb2.DetectLanguageResponse,
        )
        self.GetSupportedLanguages = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.translation.v3.TranslationService/GetSupportedLanguages',
            google.cloud.translate.v3.translation_service_pb2.GetSupportedLanguagesRequest,
            google.cloud.translate.v3.translation_service_pb2.SupportedLanguages,
        )
        self.BatchTranslateText = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.translation.v3.TranslationService/BatchTranslateText',
            google.cloud.translate.v3.translation_service_pb2.BatchTranslateTextRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateGlossary = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.translation.v3.TranslationService/CreateGlossary',
            google.cloud.translate.v3.translation_service_pb2.CreateGlossaryRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListGlossaries = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.translation.v3.TranslationService/ListGlossaries',
            google.cloud.translate.v3.translation_service_pb2.ListGlossariesRequest,
            google.cloud.translate.v3.translation_service_pb2.ListGlossariesResponse,
        )
        self.GetGlossary = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.translation.v3.TranslationService/GetGlossary',
            google.cloud.translate.v3.translation_service_pb2.GetGlossaryRequest,
            google.cloud.translate.v3.translation_service_pb2.Glossary,
        )
        self.DeleteGlossary = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.translation.v3.TranslationService/DeleteGlossary',
            google.cloud.translate.v3.translation_service_pb2.DeleteGlossaryRequest,
            google.longrunning.operations_pb2.Operation,
        )
