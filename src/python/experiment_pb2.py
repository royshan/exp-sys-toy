# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: experiment.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='experiment.proto',
  package='exp_sys',
  serialized_pb='\n\x10\x65xperiment.proto\x12\x07\x65xp_sys\"\x82\x01\n\tParameter\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12%\n\x04type\x18\x03 \x01(\x0e\x32\x17.exp_sys.Parameter.Type\"1\n\x04Type\x12\x08\n\x04\x42OOL\x10\x00\x12\x07\n\x03INT\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\n\n\x06STRING\x10\x03\"\'\n\tCondition\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\")\n\x0b\x42ucketRange\x12\r\n\x05start\x18\x01 \x02(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x02(\x05\"\x9c\x01\n\x05Layer\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\tdomain_id\x18\x03 \x01(\x05:\x01\x30\x12\x15\n\x06launch\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x13\n\x0bunbiased_id\x18\x05 \x01(\x05\x12\x1a\n\x0f\x66ixed_biased_id\x18\x06 \x01(\x05:\x01\x30\x12\x1b\n\x10random_biased_id\x18\x07 \x01(\x05:\x01\x30\"H\n\x06\x44omain\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\x06ranges\x18\x03 \x03(\x0b\x32\x14.exp_sys.BucketRange\"\x8f\x02\n\nExperiment\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08layer_id\x18\x03 \x01(\x05\x12\x12\n\ncontrol_id\x18\x04 \x01(\x05\x12\x12\n\nstart_time\x18\x05 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x06 \x01(\t\x12%\n\tdiversion\x18\x07 \x01(\x0e\x32\x12.exp_sys.Diversion\x12&\n\nparameters\x18\x08 \x03(\x0b\x32\x12.exp_sys.Parameter\x12&\n\nconditions\x18\t \x03(\x0b\x32\x12.exp_sys.Condition\x12$\n\x06ranges\x18\n \x03(\x0b\x32\x14.exp_sys.BucketRange\"\xa0\x01\n\nDeployment\x12&\n\nparameters\x18\x01 \x03(\x0b\x32\x12.exp_sys.Parameter\x12\x1e\n\x06layers\x18\x02 \x03(\x0b\x32\x0e.exp_sys.Layer\x12 \n\x07\x64omains\x18\x03 \x03(\x0b\x32\x0f.exp_sys.Domain\x12(\n\x0b\x65xperiments\x18\x04 \x03(\x0b\x32\x13.exp_sys.Experiment*7\n\tDiversion\x12\n\n\x06RANDOM\x10\x00\x12\x08\n\x04UUID\x10\x01\x12\x08\n\x04USER\x10\x02\x12\n\n\x06\x43OOKIE\x10\x03')

_DIVERSION = _descriptor.EnumDescriptor(
  name='Diversion',
  full_name='exp_sys.Diversion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RANDOM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UUID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COOKIE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=916,
  serialized_end=971,
)

Diversion = enum_type_wrapper.EnumTypeWrapper(_DIVERSION)
RANDOM = 0
UUID = 1
USER = 2
COOKIE = 3


_PARAMETER_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='exp_sys.Parameter.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=111,
  serialized_end=160,
)


_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='exp_sys.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='exp_sys.Parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='exp_sys.Parameter.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='exp_sys.Parameter.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PARAMETER_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=160,
)


_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='exp_sys.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='exp_sys.Condition.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='exp_sys.Condition.args', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=162,
  serialized_end=201,
)


_BUCKETRANGE = _descriptor.Descriptor(
  name='BucketRange',
  full_name='exp_sys.BucketRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='exp_sys.BucketRange.start', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='exp_sys.BucketRange.end', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=203,
  serialized_end=244,
)


_LAYER = _descriptor.Descriptor(
  name='Layer',
  full_name='exp_sys.Layer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='exp_sys.Layer.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='exp_sys.Layer.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='exp_sys.Layer.domain_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='launch', full_name='exp_sys.Layer.launch', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unbiased_id', full_name='exp_sys.Layer.unbiased_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fixed_biased_id', full_name='exp_sys.Layer.fixed_biased_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='random_biased_id', full_name='exp_sys.Layer.random_biased_id', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
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
  serialized_start=247,
  serialized_end=403,
)


_DOMAIN = _descriptor.Descriptor(
  name='Domain',
  full_name='exp_sys.Domain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='exp_sys.Domain.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='exp_sys.Domain.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ranges', full_name='exp_sys.Domain.ranges', index=2,
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
  serialized_start=405,
  serialized_end=477,
)


_EXPERIMENT = _descriptor.Descriptor(
  name='Experiment',
  full_name='exp_sys.Experiment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='exp_sys.Experiment.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='exp_sys.Experiment.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layer_id', full_name='exp_sys.Experiment.layer_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='control_id', full_name='exp_sys.Experiment.control_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='exp_sys.Experiment.start_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='exp_sys.Experiment.end_time', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diversion', full_name='exp_sys.Experiment.diversion', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='exp_sys.Experiment.parameters', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='exp_sys.Experiment.conditions', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ranges', full_name='exp_sys.Experiment.ranges', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=480,
  serialized_end=751,
)


_DEPLOYMENT = _descriptor.Descriptor(
  name='Deployment',
  full_name='exp_sys.Deployment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='exp_sys.Deployment.parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layers', full_name='exp_sys.Deployment.layers', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domains', full_name='exp_sys.Deployment.domains', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiments', full_name='exp_sys.Deployment.experiments', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=754,
  serialized_end=914,
)

_PARAMETER.fields_by_name['type'].enum_type = _PARAMETER_TYPE
_PARAMETER_TYPE.containing_type = _PARAMETER;
_DOMAIN.fields_by_name['ranges'].message_type = _BUCKETRANGE
_EXPERIMENT.fields_by_name['diversion'].enum_type = _DIVERSION
_EXPERIMENT.fields_by_name['parameters'].message_type = _PARAMETER
_EXPERIMENT.fields_by_name['conditions'].message_type = _CONDITION
_EXPERIMENT.fields_by_name['ranges'].message_type = _BUCKETRANGE
_DEPLOYMENT.fields_by_name['parameters'].message_type = _PARAMETER
_DEPLOYMENT.fields_by_name['layers'].message_type = _LAYER
_DEPLOYMENT.fields_by_name['domains'].message_type = _DOMAIN
_DEPLOYMENT.fields_by_name['experiments'].message_type = _EXPERIMENT
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['Condition'] = _CONDITION
DESCRIPTOR.message_types_by_name['BucketRange'] = _BUCKETRANGE
DESCRIPTOR.message_types_by_name['Layer'] = _LAYER
DESCRIPTOR.message_types_by_name['Domain'] = _DOMAIN
DESCRIPTOR.message_types_by_name['Experiment'] = _EXPERIMENT
DESCRIPTOR.message_types_by_name['Deployment'] = _DEPLOYMENT

class Parameter(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PARAMETER

  # @@protoc_insertion_point(class_scope:exp_sys.Parameter)

class Condition(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONDITION

  # @@protoc_insertion_point(class_scope:exp_sys.Condition)

class BucketRange(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BUCKETRANGE

  # @@protoc_insertion_point(class_scope:exp_sys.BucketRange)

class Layer(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LAYER

  # @@protoc_insertion_point(class_scope:exp_sys.Layer)

class Domain(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DOMAIN

  # @@protoc_insertion_point(class_scope:exp_sys.Domain)

class Experiment(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXPERIMENT

  # @@protoc_insertion_point(class_scope:exp_sys.Experiment)

class Deployment(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEPLOYMENT

  # @@protoc_insertion_point(class_scope:exp_sys.Deployment)


# @@protoc_insertion_point(module_scope)