# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/type/latlng.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/type/latlng.proto',
  package='google.type',
  syntax='proto3',
  serialized_options=b'\n\017com.google.typeB\013LatLngProtoP\001Z8google.golang.org/genproto/googleapis/type/latlng;latlng\370\001\001\242\002\003GTP',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18google/type/latlng.proto\x12\x0bgoogle.type\"-\n\x06LatLng\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x42\x63\n\x0f\x63om.google.typeB\x0bLatLngProtoP\x01Z8google.golang.org/genproto/googleapis/type/latlng;latlng\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3'
)




_LATLNG = _descriptor.Descriptor(
  name='LatLng',
  full_name='google.type.LatLng',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='google.type.LatLng.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='google.type.LatLng.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=41,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['LatLng'] = _LATLNG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LatLng = _reflection.GeneratedProtocolMessageType('LatLng', (_message.Message,), {
  'DESCRIPTOR' : _LATLNG,
  '__module__' : 'google.type.latlng_pb2'
  # @@protoc_insertion_point(class_scope:google.type.LatLng)
  })
_sym_db.RegisterMessage(LatLng)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
