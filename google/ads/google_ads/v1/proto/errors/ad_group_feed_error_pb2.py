# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/errors/ad_group_feed_error.proto

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
  name='google/ads/googleads_v1/proto/errors/ad_group_feed_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.errorsB\025AdGroupFeedErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors'),
  serialized_pb=_b('\n>google/ads/googleads_v1/proto/errors/ad_group_feed_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\xdc\x02\n\x14\x41\x64GroupFeedErrorEnum\"\xc3\x02\n\x10\x41\x64GroupFeedError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12,\n(FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE\x10\x02\x12\"\n\x1e\x43\x41NNOT_CREATE_FOR_REMOVED_FEED\x10\x03\x12\x1f\n\x1b\x41\x44GROUP_FEED_ALREADY_EXISTS\x10\x04\x12*\n&CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED\x10\x05\x12\x1c\n\x18INVALID_PLACEHOLDER_TYPE\x10\x06\x12,\n(MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE\x10\x07\x12&\n\"NO_EXISTING_LOCATION_CUSTOMER_FEED\x10\x08\x42\xf0\x01\n\"com.google.ads.googleads.v1.errorsB\x15\x41\x64GroupFeedErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ADGROUPFEEDERRORENUM_ADGROUPFEEDERROR = _descriptor.EnumDescriptor(
  name='AdGroupFeedError',
  full_name='google.ads.googleads.v1.errors.AdGroupFeedErrorEnum.AdGroupFeedError',
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
      name='FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CREATE_FOR_REMOVED_FEED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADGROUP_FEED_ALREADY_EXISTS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OPERATE_ON_REMOVED_ADGROUP_FEED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLACEHOLDER_TYPE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_EXISTING_LOCATION_CUSTOMER_FEED', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=477,
)
_sym_db.RegisterEnumDescriptor(_ADGROUPFEEDERRORENUM_ADGROUPFEEDERROR)


_ADGROUPFEEDERRORENUM = _descriptor.Descriptor(
  name='AdGroupFeedErrorEnum',
  full_name='google.ads.googleads.v1.errors.AdGroupFeedErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADGROUPFEEDERRORENUM_ADGROUPFEEDERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=477,
)

_ADGROUPFEEDERRORENUM_ADGROUPFEEDERROR.containing_type = _ADGROUPFEEDERRORENUM
DESCRIPTOR.message_types_by_name['AdGroupFeedErrorEnum'] = _ADGROUPFEEDERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupFeedErrorEnum = _reflection.GeneratedProtocolMessageType('AdGroupFeedErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPFEEDERRORENUM,
  __module__ = 'google.ads.googleads_v1.proto.errors.ad_group_feed_error_pb2'
  ,
  __doc__ = """Container for enum describing possible ad group feed errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.AdGroupFeedErrorEnum)
  ))
_sym_db.RegisterMessage(AdGroupFeedErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
