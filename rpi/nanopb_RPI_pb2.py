# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nanopb_RPI.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nanopb_RPI.proto',
  package='',
  serialized_pb=_b('\n\x10nanopb_RPI.proto\"@\n\nSensorData\x12\r\n\x05value\x18\x01 \x02(\x02\x12\x10\n\x08sensorId\x18\x02 \x02(\x05\x12\x11\n\ttimestamp\x18\x03 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SENSORDATA = _descriptor.Descriptor(
  name='SensorData',
  full_name='SensorData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='SensorData.value', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sensorId', full_name='SensorData.sensorId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='SensorData.timestamp', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['SensorData'] = _SENSORDATA

SensorData = _reflection.GeneratedProtocolMessageType('SensorData', (_message.Message,), dict(
  DESCRIPTOR = _SENSORDATA,
  __module__ = 'nanopb_RPI_pb2'
  # @@protoc_insertion_point(class_scope:SensorData)
  ))
_sym_db.RegisterMessage(SensorData)


# @@protoc_insertion_point(module_scope)
