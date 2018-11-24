# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='options.proto',
  package='is',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\roptions.proto\x12\x02is\"\xa1\x01\n#ObjectAnnotationsTransformerOptions\x12\x12\n\nbroker_uri\x18\x01 \x01(\t\x12\x13\n\x0bzipkin_host\x18\x02 \x01(\t\x12\x13\n\x0bzipkin_port\x18\x03 \x01(\r\x12\x14\n\x0cinput_topics\x18\x04 \x03(\t\x12\x14\n\x0coutput_topic\x18\x05 \x01(\t\x12\x10\n\x08\x66rame_id\x18\x06 \x01(\x03\x62\x06proto3')
)




_OBJECTANNOTATIONSTRANSFORMEROPTIONS = _descriptor.Descriptor(
  name='ObjectAnnotationsTransformerOptions',
  full_name='is.ObjectAnnotationsTransformerOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='broker_uri', full_name='is.ObjectAnnotationsTransformerOptions.broker_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zipkin_host', full_name='is.ObjectAnnotationsTransformerOptions.zipkin_host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zipkin_port', full_name='is.ObjectAnnotationsTransformerOptions.zipkin_port', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_topics', full_name='is.ObjectAnnotationsTransformerOptions.input_topics', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_topic', full_name='is.ObjectAnnotationsTransformerOptions.output_topic', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_id', full_name='is.ObjectAnnotationsTransformerOptions.frame_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=22,
  serialized_end=183,
)

DESCRIPTOR.message_types_by_name['ObjectAnnotationsTransformerOptions'] = _OBJECTANNOTATIONSTRANSFORMEROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObjectAnnotationsTransformerOptions = _reflection.GeneratedProtocolMessageType('ObjectAnnotationsTransformerOptions', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTANNOTATIONSTRANSFORMEROPTIONS,
  __module__ = 'options_pb2'
  # @@protoc_insertion_point(class_scope:is.ObjectAnnotationsTransformerOptions)
  ))
_sym_db.RegisterMessage(ObjectAnnotationsTransformerOptions)


# @@protoc_insertion_point(module_scope)
