# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/mobile_app_category_constant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/mobile_app_category_constant.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\036MobileAppCategoryConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\nJgoogle/ads/googleads_v1/proto/resources/mobile_app_category_constant.proto\x12!google.ads.googleads.v1.resources\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\x87\x01\n\x19MobileAppCategoryConstant\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x8b\x02\n%com.google.ads.googleads.v1.resourcesB\x1eMobileAppCategoryConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_MOBILEAPPCATEGORYCONSTANT = _descriptor.Descriptor(
  name='MobileAppCategoryConstant',
  full_name='google.ads.googleads.v1.resources.MobileAppCategoryConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.MobileAppCategoryConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v1.resources.MobileAppCategoryConstant.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v1.resources.MobileAppCategoryConstant.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=176,
  serialized_end=311,
)

_MOBILEAPPCATEGORYCONSTANT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MOBILEAPPCATEGORYCONSTANT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['MobileAppCategoryConstant'] = _MOBILEAPPCATEGORYCONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MobileAppCategoryConstant = _reflection.GeneratedProtocolMessageType('MobileAppCategoryConstant', (_message.Message,), dict(
  DESCRIPTOR = _MOBILEAPPCATEGORYCONSTANT,
  __module__ = 'google.ads.googleads_v1.proto.resources.mobile_app_category_constant_pb2'
  ,
  __doc__ = """A mobile application category constant.
  
  
  Attributes:
      resource_name:
          The resource name of the mobile app category constant. Mobile
          app category constant resource names have the form:
          ``mobileAppCategoryConstants/{mobile_app_category_id}``
      id:
          The ID of the mobile app category constant.
      name:
          Mobile app category name.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.MobileAppCategoryConstant)
  ))
_sym_db.RegisterMessage(MobileAppCategoryConstant)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
