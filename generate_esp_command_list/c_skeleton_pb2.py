# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: c_skeleton.proto

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
  name='c_skeleton.proto',
  package='c_skeleton',
  serialized_pb=_b('\n\x10\x63_skeleton.proto\x12\nc_skeleton\"/\n\tArguments\x12\x10\n\x08\x61rgument\x18\x01 \x02(\t\x12\x10\n\x08\x61rg_type\x18\x02 \x02(\t\"\x12\n\x04\x42\x61se\x12\n\n\x02\x66n\x18\x01 \x02(\t\"a\n\x03\x43\x66n\x12\n\n\x02id\x18\x01 \x02(\x05\x12!\n\x07\x62\x61se_fn\x18\x02 \x02(\x0b\x32\x10.c_skeleton.Base\x12+\n\x0c\x66n_arguments\x18\x03 \x03(\x0b\x32\x15.c_skeleton.Arguments\"%\n\x04\x43\x66ns\x12\x1d\n\x04\x63_fn\x18\x01 \x03(\x0b\x32\x0f.c_skeleton.Cfn')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ARGUMENTS = _descriptor.Descriptor(
  name='Arguments',
  full_name='c_skeleton.Arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='argument', full_name='c_skeleton.Arguments.argument', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arg_type', full_name='c_skeleton.Arguments.arg_type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=32,
  serialized_end=79,
)


_BASE = _descriptor.Descriptor(
  name='Base',
  full_name='c_skeleton.Base',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fn', full_name='c_skeleton.Base.fn', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=81,
  serialized_end=99,
)


_CFN = _descriptor.Descriptor(
  name='Cfn',
  full_name='c_skeleton.Cfn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='c_skeleton.Cfn.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_fn', full_name='c_skeleton.Cfn.base_fn', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fn_arguments', full_name='c_skeleton.Cfn.fn_arguments', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=101,
  serialized_end=198,
)


_CFNS = _descriptor.Descriptor(
  name='Cfns',
  full_name='c_skeleton.Cfns',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c_fn', full_name='c_skeleton.Cfns.c_fn', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=200,
  serialized_end=237,
)

_CFN.fields_by_name['base_fn'].message_type = _BASE
_CFN.fields_by_name['fn_arguments'].message_type = _ARGUMENTS
_CFNS.fields_by_name['c_fn'].message_type = _CFN
DESCRIPTOR.message_types_by_name['Arguments'] = _ARGUMENTS
DESCRIPTOR.message_types_by_name['Base'] = _BASE
DESCRIPTOR.message_types_by_name['Cfn'] = _CFN
DESCRIPTOR.message_types_by_name['Cfns'] = _CFNS

Arguments = _reflection.GeneratedProtocolMessageType('Arguments', (_message.Message,), dict(
  DESCRIPTOR = _ARGUMENTS,
  __module__ = 'c_skeleton_pb2'
  # @@protoc_insertion_point(class_scope:c_skeleton.Arguments)
  ))
_sym_db.RegisterMessage(Arguments)

Base = _reflection.GeneratedProtocolMessageType('Base', (_message.Message,), dict(
  DESCRIPTOR = _BASE,
  __module__ = 'c_skeleton_pb2'
  # @@protoc_insertion_point(class_scope:c_skeleton.Base)
  ))
_sym_db.RegisterMessage(Base)

Cfn = _reflection.GeneratedProtocolMessageType('Cfn', (_message.Message,), dict(
  DESCRIPTOR = _CFN,
  __module__ = 'c_skeleton_pb2'
  # @@protoc_insertion_point(class_scope:c_skeleton.Cfn)
  ))
_sym_db.RegisterMessage(Cfn)

Cfns = _reflection.GeneratedProtocolMessageType('Cfns', (_message.Message,), dict(
  DESCRIPTOR = _CFNS,
  __module__ = 'c_skeleton_pb2'
  # @@protoc_insertion_point(class_scope:c_skeleton.Cfns)
  ))
_sym_db.RegisterMessage(Cfns)


# @@protoc_insertion_point(module_scope)