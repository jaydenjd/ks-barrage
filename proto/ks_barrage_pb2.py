# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/ks_barrage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/ks_barrage.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16proto/ks_barrage.proto\"b\n\x0e\x42\x61rrageContent\x12\x14\n\x0c\x61udience_num\x18\x01 \x01(\t\x12\x10\n\x08like_num\x18\x02 \x01(\t\x12(\n\x0f\x62\x61rrage_message\x18\x05 \x03(\x0b\x32\x0f.BarrageMessage\"~\n\x0e\x42\x61rrageMessage\x12\x1b\n\x08\x61udience\x18\x02 \x01(\x0b\x32\t.Audience\x12\x17\n\x0f\x63omment_content\x18\x03 \x01(\t\x12\x12\n\nbarrage_id\x18\x04 \x01(\t\x12\"\n\x0c\x63ontent_type\x18\x07 \x01(\x0e\x32\x0c.ContentType\"\x0e\n\x0c\x41udienceRank\"9\n\x08\x41udience\x12\x0b\n\x03\x65id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\navatar_url\x18\x03 \x01(\t\"z\n\x07\x42\x61rrage\x12\"\n\x0c\x42\x61rrage_type\x18\x01 \x01(\x0e\x32\x0c.BarrageType\x12\x0e\n\x06status\x18\x02 \x01(\x03\x12(\n\x0f\x62\x61rrage_content\x18\x03 \x01(\x0b\x32\x0f.BarrageContent\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\"u\n\x07Request\x12\x0e\n\x06status\x18\x01 \x01(\x03\x12\x1f\n\x06params\x18\x03 \x01(\x0b\x32\x0f.Request.Params\x1a\x39\n\x06Params\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07live_id\x18\x02 \x01(\t\x12\x0f\n\x07page_id\x18\x07 \x01(\t\"g\n\x0fHeartbeatClient\x12\x0e\n\x06status\x18\x01 \x01(\x03\x12\'\n\x06params\x18\x03 \x01(\x0b\x32\x17.HeartbeatClient.Params\x1a\x1b\n\x06Params\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\"D\n\x0eResponseCommon\x12\"\n\x0c\x62\x61rrage_type\x18\x01 \x01(\x0e\x32\x0c.BarrageType\x12\x0e\n\x06status\x18\x02 \x01(\x03*9\n\x0b\x43ontentType\x12\x13\n\x0fUNKNOWN_CONTENT\x10\x00\x12\x0b\n\x07\x43OMMENT\x10\x01\x12\x08\n\x04LIKE\x10\x02*p\n\x0b\x42\x61rrageType\x12\x18\n\x14\x42\x41RRAGE_TYPE_UNKNOWN\x10\x00\x12\r\n\tHEARTBEAT\x10\x65\x12\x16\n\x11\x43ONNECTED_SUCCESS\x10\xac\x02\x12\x0c\n\x07\x42\x41RRAGE\x10\xb6\x02\x12\x12\n\rAUDIENCE_RANK\x10\xd4\x02\x62\x06proto3'
)

_CONTENTTYPE = _descriptor.EnumDescriptor(
  name='ContentType',
  full_name='ContentType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CONTENT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMMENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LIKE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=747,
  serialized_end=804,
)
_sym_db.RegisterEnumDescriptor(_CONTENTTYPE)

ContentType = enum_type_wrapper.EnumTypeWrapper(_CONTENTTYPE)
_BARRAGETYPE = _descriptor.EnumDescriptor(
  name='BarrageType',
  full_name='BarrageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BARRAGE_TYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HEARTBEAT', index=1, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONNECTED_SUCCESS', index=2, number=300,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BARRAGE', index=3, number=310,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AUDIENCE_RANK', index=4, number=340,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=806,
  serialized_end=918,
)
_sym_db.RegisterEnumDescriptor(_BARRAGETYPE)

BarrageType = enum_type_wrapper.EnumTypeWrapper(_BARRAGETYPE)
UNKNOWN_CONTENT = 0
COMMENT = 1
LIKE = 2
BARRAGE_TYPE_UNKNOWN = 0
HEARTBEAT = 101
CONNECTED_SUCCESS = 300
BARRAGE = 310
AUDIENCE_RANK = 340



_BARRAGECONTENT = _descriptor.Descriptor(
  name='BarrageContent',
  full_name='BarrageContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audience_num', full_name='BarrageContent.audience_num', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='like_num', full_name='BarrageContent.like_num', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='barrage_message', full_name='BarrageContent.barrage_message', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=26,
  serialized_end=124,
)


_BARRAGEMESSAGE = _descriptor.Descriptor(
  name='BarrageMessage',
  full_name='BarrageMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audience', full_name='BarrageMessage.audience', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comment_content', full_name='BarrageMessage.comment_content', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='barrage_id', full_name='BarrageMessage.barrage_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='BarrageMessage.content_type', index=3,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=126,
  serialized_end=252,
)


_AUDIENCERANK = _descriptor.Descriptor(
  name='AudienceRank',
  full_name='AudienceRank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=254,
  serialized_end=268,
)


_AUDIENCE = _descriptor.Descriptor(
  name='Audience',
  full_name='Audience',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eid', full_name='Audience.eid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Audience.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='avatar_url', full_name='Audience.avatar_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=270,
  serialized_end=327,
)


_BARRAGE = _descriptor.Descriptor(
  name='Barrage',
  full_name='Barrage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Barrage_type', full_name='Barrage.Barrage_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='Barrage.status', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='barrage_content', full_name='Barrage.barrage_content', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Barrage.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=329,
  serialized_end=451,
)


_REQUEST_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='Request.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='Request.Params.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='live_id', full_name='Request.Params.live_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_id', full_name='Request.Params.page_id', index=2,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=513,
  serialized_end=570,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Request.status', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='Request.params', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_PARAMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=453,
  serialized_end=570,
)


_HEARTBEATCLIENT_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='HeartbeatClient.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='HeartbeatClient.Params.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=648,
  serialized_end=675,
)

_HEARTBEATCLIENT = _descriptor.Descriptor(
  name='HeartbeatClient',
  full_name='HeartbeatClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='HeartbeatClient.status', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='HeartbeatClient.params', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HEARTBEATCLIENT_PARAMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=572,
  serialized_end=675,
)


_RESPONSECOMMON = _descriptor.Descriptor(
  name='ResponseCommon',
  full_name='ResponseCommon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='barrage_type', full_name='ResponseCommon.barrage_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='ResponseCommon.status', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=677,
  serialized_end=745,
)

_BARRAGECONTENT.fields_by_name['barrage_message'].message_type = _BARRAGEMESSAGE
_BARRAGEMESSAGE.fields_by_name['audience'].message_type = _AUDIENCE
_BARRAGEMESSAGE.fields_by_name['content_type'].enum_type = _CONTENTTYPE
_BARRAGE.fields_by_name['Barrage_type'].enum_type = _BARRAGETYPE
_BARRAGE.fields_by_name['barrage_content'].message_type = _BARRAGECONTENT
_REQUEST_PARAMS.containing_type = _REQUEST
_REQUEST.fields_by_name['params'].message_type = _REQUEST_PARAMS
_HEARTBEATCLIENT_PARAMS.containing_type = _HEARTBEATCLIENT
_HEARTBEATCLIENT.fields_by_name['params'].message_type = _HEARTBEATCLIENT_PARAMS
_RESPONSECOMMON.fields_by_name['barrage_type'].enum_type = _BARRAGETYPE
DESCRIPTOR.message_types_by_name['BarrageContent'] = _BARRAGECONTENT
DESCRIPTOR.message_types_by_name['BarrageMessage'] = _BARRAGEMESSAGE
DESCRIPTOR.message_types_by_name['AudienceRank'] = _AUDIENCERANK
DESCRIPTOR.message_types_by_name['Audience'] = _AUDIENCE
DESCRIPTOR.message_types_by_name['Barrage'] = _BARRAGE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['HeartbeatClient'] = _HEARTBEATCLIENT
DESCRIPTOR.message_types_by_name['ResponseCommon'] = _RESPONSECOMMON
DESCRIPTOR.enum_types_by_name['ContentType'] = _CONTENTTYPE
DESCRIPTOR.enum_types_by_name['BarrageType'] = _BARRAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BarrageContent = _reflection.GeneratedProtocolMessageType('BarrageContent', (_message.Message,), {
  'DESCRIPTOR' : _BARRAGECONTENT,
  '__module__' : 'proto.ks_barrage_pb2'
  # @@protoc_insertion_point(class_scope:BarrageContent)
  })
_sym_db.RegisterMessage(BarrageContent)

BarrageMessage = _reflection.GeneratedProtocolMessageType('BarrageMessage', (_message.Message,), {
  'DESCRIPTOR' : _BARRAGEMESSAGE,
  '__module__' : 'proto.ks_barrage_pb2'
  # @@protoc_insertion_point(class_scope:BarrageMessage)
  })
_sym_db.RegisterMessage(BarrageMessage)

AudienceRank = _reflection.GeneratedProtocolMessageType('AudienceRank', (_message.Message,), {
  'DESCRIPTOR' : _AUDIENCERANK,
  '__module__' : 'proto.ks_barrage_pb2'
  # @@protoc_insertion_point(class_scope:AudienceRank)
  })
_sym_db.RegisterMessage(AudienceRank)

Audience = _reflection.GeneratedProtocolMessageType('Audience', (_message.Message,), {
  'DESCRIPTOR' : _AUDIENCE,
  '__module__' : 'proto.ks_barrage_pb2'
  # @@protoc_insertion_point(class_scope:Audience)
  })
_sym_db.RegisterMessage(Audience)

Barrage = _reflection.GeneratedProtocolMessageType('Barrage', (_message.Message,), {
  'DESCRIPTOR' : _BARRAGE,
  '__module__' : 'proto.ks_barrage_pb2'
  # @@protoc_insertion_point(class_scope:Barrage)
  })
_sym_db.RegisterMessage(Barrage)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _REQUEST_PARAMS,
    '__module__' : 'proto.ks_barrage_pb2'
    # @@protoc_insertion_point(class_scope:Request.Params)
    })
  ,
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'proto.ks_barrage_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.Params)

HeartbeatClient = _reflection.GeneratedProtocolMessageType('HeartbeatClient', (_message.Message,), {

  'Params' : _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
    'DESCRIPTOR' : _HEARTBEATCLIENT_PARAMS,
    '__module__' : 'proto.ks_barrage_pb2'
    # @@protoc_insertion_point(class_scope:HeartbeatClient.Params)
    })
  ,
  'DESCRIPTOR' : _HEARTBEATCLIENT,
  '__module__' : 'proto.ks_barrage_pb2'
  # @@protoc_insertion_point(class_scope:HeartbeatClient)
  })
_sym_db.RegisterMessage(HeartbeatClient)
_sym_db.RegisterMessage(HeartbeatClient.Params)

ResponseCommon = _reflection.GeneratedProtocolMessageType('ResponseCommon', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSECOMMON,
  '__module__' : 'proto.ks_barrage_pb2'
  # @@protoc_insertion_point(class_scope:ResponseCommon)
  })
_sym_db.RegisterMessage(ResponseCommon)


# @@protoc_insertion_point(module_scope)
