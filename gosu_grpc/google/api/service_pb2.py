# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gosu_grpc.google.api import auth_pb2 as google_dot_api_dot_auth__pb2
from gosu_grpc.google.api import backend_pb2 as google_dot_api_dot_backend__pb2
from gosu_grpc.google.api import billing_pb2 as google_dot_api_dot_billing__pb2
from gosu_grpc.google.api import context_pb2 as google_dot_api_dot_context__pb2
from gosu_grpc.google.api import control_pb2 as google_dot_api_dot_control__pb2
from gosu_grpc.google.api import documentation_pb2 as google_dot_api_dot_documentation__pb2
from gosu_grpc.google.api import endpoint_pb2 as google_dot_api_dot_endpoint__pb2
from gosu_grpc.google.api import http_pb2 as google_dot_api_dot_http__pb2
from gosu_grpc.google.api import label_pb2 as google_dot_api_dot_label__pb2
from gosu_grpc.google.api import log_pb2 as google_dot_api_dot_log__pb2
from gosu_grpc.google.api import logging_pb2 as google_dot_api_dot_logging__pb2
from gosu_grpc.google.api import metric_pb2 as google_dot_api_dot_metric__pb2
from gosu_grpc.google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from gosu_grpc.google.api import monitoring_pb2 as google_dot_api_dot_monitoring__pb2
from gosu_grpc.google.api import quota_pb2 as google_dot_api_dot_quota__pb2
from gosu_grpc.google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from gosu_grpc.google.api import source_info_pb2 as google_dot_api_dot_source__info__pb2
from gosu_grpc.google.api import system_parameter_pb2 as google_dot_api_dot_system__parameter__pb2
from gosu_grpc.google.api import usage_pb2 as google_dot_api_dot_usage__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import api_pb2 as google_dot_protobuf_dot_api__pb2
from google.protobuf import type_pb2 as google_dot_protobuf_dot_type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/service.proto',
  package='google.api',
  syntax='proto3',
  serialized_options=b'\n\016com.google.apiB\014ServiceProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18google/api/service.proto\x12\ngoogle.api\x1a\x15google/api/auth.proto\x1a\x18google/api/backend.proto\x1a\x18google/api/billing.proto\x1a\x18google/api/context.proto\x1a\x18google/api/control.proto\x1a\x1egoogle/api/documentation.proto\x1a\x19google/api/endpoint.proto\x1a\x15google/api/http.proto\x1a\x16google/api/label.proto\x1a\x14google/api/log.proto\x1a\x18google/api/logging.proto\x1a\x17google/api/metric.proto\x1a#google/api/monitored_resource.proto\x1a\x1bgoogle/api/monitoring.proto\x1a\x16google/api/quota.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/source_info.proto\x1a!google/api/system_parameter.proto\x1a\x16google/api/usage.proto\x1a\x19google/protobuf/any.proto\x1a\x19google/protobuf/api.proto\x1a\x1agoogle/protobuf/type.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xd6\x07\n\x07Service\x12\x34\n\x0e\x63onfig_version\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18! \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x1b\n\x13producer_project_id\x18\x16 \x01(\t\x12\"\n\x04\x61pis\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Api\x12$\n\x05types\x18\x04 \x03(\x0b\x32\x15.google.protobuf.Type\x12$\n\x05\x65nums\x18\x05 \x03(\x0b\x32\x15.google.protobuf.Enum\x12\x30\n\rdocumentation\x18\x06 \x01(\x0b\x32\x19.google.api.Documentation\x12$\n\x07\x62\x61\x63kend\x18\x08 \x01(\x0b\x32\x13.google.api.Backend\x12\x1e\n\x04http\x18\t \x01(\x0b\x32\x10.google.api.Http\x12 \n\x05quota\x18\n \x01(\x0b\x32\x11.google.api.Quota\x12\x32\n\x0e\x61uthentication\x18\x0b \x01(\x0b\x32\x1a.google.api.Authentication\x12$\n\x07\x63ontext\x18\x0c \x01(\x0b\x32\x13.google.api.Context\x12 \n\x05usage\x18\x0f \x01(\x0b\x32\x11.google.api.Usage\x12\'\n\tendpoints\x18\x12 \x03(\x0b\x32\x14.google.api.Endpoint\x12$\n\x07\x63ontrol\x18\x15 \x01(\x0b\x32\x13.google.api.Control\x12\'\n\x04logs\x18\x17 \x03(\x0b\x32\x19.google.api.LogDescriptor\x12-\n\x07metrics\x18\x18 \x03(\x0b\x32\x1c.google.api.MetricDescriptor\x12\x44\n\x13monitored_resources\x18\x19 \x03(\x0b\x32\'.google.api.MonitoredResourceDescriptor\x12$\n\x07\x62illing\x18\x1a \x01(\x0b\x32\x13.google.api.Billing\x12$\n\x07logging\x18\x1b \x01(\x0b\x32\x13.google.api.Logging\x12*\n\nmonitoring\x18\x1c \x01(\x0b\x32\x16.google.api.Monitoring\x12\x37\n\x11system_parameters\x18\x1d \x01(\x0b\x32\x1c.google.api.SystemParameters\x12+\n\x0bsource_info\x18% \x01(\x0b\x32\x16.google.api.SourceInfoBn\n\x0e\x63om.google.apiB\x0cServiceProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_auth__pb2.DESCRIPTOR,google_dot_api_dot_backend__pb2.DESCRIPTOR,google_dot_api_dot_billing__pb2.DESCRIPTOR,google_dot_api_dot_context__pb2.DESCRIPTOR,google_dot_api_dot_control__pb2.DESCRIPTOR,google_dot_api_dot_documentation__pb2.DESCRIPTOR,google_dot_api_dot_endpoint__pb2.DESCRIPTOR,google_dot_api_dot_http__pb2.DESCRIPTOR,google_dot_api_dot_label__pb2.DESCRIPTOR,google_dot_api_dot_log__pb2.DESCRIPTOR,google_dot_api_dot_logging__pb2.DESCRIPTOR,google_dot_api_dot_metric__pb2.DESCRIPTOR,google_dot_api_dot_monitored__resource__pb2.DESCRIPTOR,google_dot_api_dot_monitoring__pb2.DESCRIPTOR,google_dot_api_dot_quota__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_source__info__pb2.DESCRIPTOR,google_dot_api_dot_system__parameter__pb2.DESCRIPTOR,google_dot_api_dot_usage__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_api__pb2.DESCRIPTOR,google_dot_protobuf_dot_type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='google.api.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_version', full_name='google.api.Service.config_version', index=0,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.api.Service.name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.api.Service.id', index=2,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='google.api.Service.title', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='producer_project_id', full_name='google.api.Service.producer_project_id', index=4,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='apis', full_name='google.api.Service.apis', index=5,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='types', full_name='google.api.Service.types', index=6,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enums', full_name='google.api.Service.enums', index=7,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='documentation', full_name='google.api.Service.documentation', index=8,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backend', full_name='google.api.Service.backend', index=9,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='http', full_name='google.api.Service.http', index=10,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quota', full_name='google.api.Service.quota', index=11,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authentication', full_name='google.api.Service.authentication', index=12,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='context', full_name='google.api.Service.context', index=13,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usage', full_name='google.api.Service.usage', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='google.api.Service.endpoints', index=15,
      number=18, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='control', full_name='google.api.Service.control', index=16,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs', full_name='google.api.Service.logs', index=17,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='google.api.Service.metrics', index=18,
      number=24, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monitored_resources', full_name='google.api.Service.monitored_resources', index=19,
      number=25, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='billing', full_name='google.api.Service.billing', index=20,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logging', full_name='google.api.Service.logging', index=21,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monitoring', full_name='google.api.Service.monitoring', index=22,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system_parameters', full_name='google.api.Service.system_parameters', index=23,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_info', full_name='google.api.Service.source_info', index=24,
      number=37, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=667,
  serialized_end=1649,
)

_SERVICE.fields_by_name['config_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_SERVICE.fields_by_name['apis'].message_type = google_dot_protobuf_dot_api__pb2._API
_SERVICE.fields_by_name['types'].message_type = google_dot_protobuf_dot_type__pb2._TYPE
_SERVICE.fields_by_name['enums'].message_type = google_dot_protobuf_dot_type__pb2._ENUM
_SERVICE.fields_by_name['documentation'].message_type = google_dot_api_dot_documentation__pb2._DOCUMENTATION
_SERVICE.fields_by_name['backend'].message_type = google_dot_api_dot_backend__pb2._BACKEND
_SERVICE.fields_by_name['http'].message_type = google_dot_api_dot_http__pb2._HTTP
_SERVICE.fields_by_name['quota'].message_type = google_dot_api_dot_quota__pb2._QUOTA
_SERVICE.fields_by_name['authentication'].message_type = google_dot_api_dot_auth__pb2._AUTHENTICATION
_SERVICE.fields_by_name['context'].message_type = google_dot_api_dot_context__pb2._CONTEXT
_SERVICE.fields_by_name['usage'].message_type = google_dot_api_dot_usage__pb2._USAGE
_SERVICE.fields_by_name['endpoints'].message_type = google_dot_api_dot_endpoint__pb2._ENDPOINT
_SERVICE.fields_by_name['control'].message_type = google_dot_api_dot_control__pb2._CONTROL
_SERVICE.fields_by_name['logs'].message_type = google_dot_api_dot_log__pb2._LOGDESCRIPTOR
_SERVICE.fields_by_name['metrics'].message_type = google_dot_api_dot_metric__pb2._METRICDESCRIPTOR
_SERVICE.fields_by_name['monitored_resources'].message_type = google_dot_api_dot_monitored__resource__pb2._MONITOREDRESOURCEDESCRIPTOR
_SERVICE.fields_by_name['billing'].message_type = google_dot_api_dot_billing__pb2._BILLING
_SERVICE.fields_by_name['logging'].message_type = google_dot_api_dot_logging__pb2._LOGGING
_SERVICE.fields_by_name['monitoring'].message_type = google_dot_api_dot_monitoring__pb2._MONITORING
_SERVICE.fields_by_name['system_parameters'].message_type = google_dot_api_dot_system__parameter__pb2._SYSTEMPARAMETERS
_SERVICE.fields_by_name['source_info'].message_type = google_dot_api_dot_source__info__pb2._SOURCEINFO
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'google.api.service_pb2'
  # @@protoc_insertion_point(class_scope:google.api.Service)
  })
_sym_db.RegisterMessage(Service)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
