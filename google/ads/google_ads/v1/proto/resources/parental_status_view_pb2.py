# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/parental_status_view.proto

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
  name='google/ads/googleads_v1/proto/resources/parental_status_view.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\027ParentalStatusViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\nBgoogle/ads/googleads_v1/proto/resources/parental_status_view.proto\x12!google.ads.googleads.v1.resources\x1a\x1cgoogle/api/annotations.proto\"+\n\x12ParentalStatusView\x12\x15\n\rresource_name\x18\x01 \x01(\tB\x84\x02\n%com.google.ads.googleads.v1.resourcesB\x17ParentalStatusViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_PARENTALSTATUSVIEW = _descriptor.Descriptor(
  name='ParentalStatusView',
  full_name='google.ads.googleads.v1.resources.ParentalStatusView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.ParentalStatusView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=135,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['ParentalStatusView'] = _PARENTALSTATUSVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParentalStatusView = _reflection.GeneratedProtocolMessageType('ParentalStatusView', (_message.Message,), dict(
  DESCRIPTOR = _PARENTALSTATUSVIEW,
  __module__ = 'google.ads.googleads_v1.proto.resources.parental_status_view_pb2'
  ,
  __doc__ = """A parental status view.
  
  
  Attributes:
      resource_name:
          The resource name of the parental status view. Parental Status
          view resource names have the form:  ``customers/{customer_id}/
          parentalStatusViews/{ad_group_id}~{criterion_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.ParentalStatusView)
  ))
_sym_db.RegisterMessage(ParentalStatusView)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
