# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/errors/string_format_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/errors/string_format_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.errorsB\026StringFormatErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors'),
  serialized_pb=_b('\n>google/ads/googleads_v1/proto/errors/string_format_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"q\n\x15StringFormatErrorEnum\"X\n\x11StringFormatError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x11\n\rILLEGAL_CHARS\x10\x02\x12\x12\n\x0eINVALID_FORMAT\x10\x03\x42\xf1\x01\n\"com.google.ads.googleads.v1.errorsB\x16StringFormatErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_STRINGFORMATERRORENUM_STRINGFORMATERROR = _descriptor.EnumDescriptor(
  name='StringFormatError',
  full_name='google.ads.googleads.v1.errors.StringFormatErrorEnum.StringFormatError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_CHARS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FORMAT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=153,
  serialized_end=241,
)
_sym_db.RegisterEnumDescriptor(_STRINGFORMATERRORENUM_STRINGFORMATERROR)


_STRINGFORMATERRORENUM = _descriptor.Descriptor(
  name='StringFormatErrorEnum',
  full_name='google.ads.googleads.v1.errors.StringFormatErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STRINGFORMATERRORENUM_STRINGFORMATERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=241,
)

_STRINGFORMATERRORENUM_STRINGFORMATERROR.containing_type = _STRINGFORMATERRORENUM
DESCRIPTOR.message_types_by_name['StringFormatErrorEnum'] = _STRINGFORMATERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringFormatErrorEnum = _reflection.GeneratedProtocolMessageType('StringFormatErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _STRINGFORMATERRORENUM,
  __module__ = 'google.ads.googleads_v1.proto.errors.string_format_error_pb2'
  ,
  __doc__ = """Container for enum describing possible string format errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.StringFormatErrorEnum)
  ))
_sym_db.RegisterMessage(StringFormatErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
