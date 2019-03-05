# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/common/simulation.proto

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
  name='google/ads/googleads_v1/proto/common/simulation.proto',
  package='google.ads.googleads.v1.common',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.commonB\017SimulationProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Common\312\002\036Google\\Ads\\GoogleAds\\V1\\Common\352\002\"Google::Ads::GoogleAds::V1::Common'),
  serialized_pb=_b('\n5google/ads/googleads_v1/proto/common/simulation.proto\x12\x1egoogle.ads.googleads.v1.common\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"l\n\x1e\x42idModifierSimulationPointList\x12J\n\x06points\x18\x01 \x03(\x0b\x32:.google.ads.googleads.v1.common.BidModifierSimulationPoint\"\x9a\x03\n\x1a\x42idModifierSimulationPoint\x12\x32\n\x0c\x62id_modifier\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12:\n\x14\x62iddable_conversions\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12@\n\x1a\x62iddable_conversions_value\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x06\x63licks\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x30\n\x0b\x63ost_micros\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x30\n\x0bimpressions\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x14top_slot_impressions\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\xea\x01\n\"com.google.ads.googleads.v1.commonB\x0fSimulationProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Common\xea\x02\"Google::Ads::GoogleAds::V1::Commonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_BIDMODIFIERSIMULATIONPOINTLIST = _descriptor.Descriptor(
  name='BidModifierSimulationPointList',
  full_name='google.ads.googleads.v1.common.BidModifierSimulationPointList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='google.ads.googleads.v1.common.BidModifierSimulationPointList.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=151,
  serialized_end=259,
)


_BIDMODIFIERSIMULATIONPOINT = _descriptor.Descriptor(
  name='BidModifierSimulationPoint',
  full_name='google.ads.googleads.v1.common.BidModifierSimulationPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bid_modifier', full_name='google.ads.googleads.v1.common.BidModifierSimulationPoint.bid_modifier', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='biddable_conversions', full_name='google.ads.googleads.v1.common.BidModifierSimulationPoint.biddable_conversions', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='biddable_conversions_value', full_name='google.ads.googleads.v1.common.BidModifierSimulationPoint.biddable_conversions_value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clicks', full_name='google.ads.googleads.v1.common.BidModifierSimulationPoint.clicks', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost_micros', full_name='google.ads.googleads.v1.common.BidModifierSimulationPoint.cost_micros', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='impressions', full_name='google.ads.googleads.v1.common.BidModifierSimulationPoint.impressions', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_slot_impressions', full_name='google.ads.googleads.v1.common.BidModifierSimulationPoint.top_slot_impressions', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=262,
  serialized_end=672,
)

_BIDMODIFIERSIMULATIONPOINTLIST.fields_by_name['points'].message_type = _BIDMODIFIERSIMULATIONPOINT
_BIDMODIFIERSIMULATIONPOINT.fields_by_name['bid_modifier'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_BIDMODIFIERSIMULATIONPOINT.fields_by_name['biddable_conversions'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_BIDMODIFIERSIMULATIONPOINT.fields_by_name['biddable_conversions_value'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_BIDMODIFIERSIMULATIONPOINT.fields_by_name['clicks'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BIDMODIFIERSIMULATIONPOINT.fields_by_name['cost_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BIDMODIFIERSIMULATIONPOINT.fields_by_name['impressions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_BIDMODIFIERSIMULATIONPOINT.fields_by_name['top_slot_impressions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['BidModifierSimulationPointList'] = _BIDMODIFIERSIMULATIONPOINTLIST
DESCRIPTOR.message_types_by_name['BidModifierSimulationPoint'] = _BIDMODIFIERSIMULATIONPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BidModifierSimulationPointList = _reflection.GeneratedProtocolMessageType('BidModifierSimulationPointList', (_message.Message,), dict(
  DESCRIPTOR = _BIDMODIFIERSIMULATIONPOINTLIST,
  __module__ = 'google.ads.googleads_v1.proto.common.simulation_pb2'
  ,
  __doc__ = """A container for simulation points for simulations of type BID\_MODIFIER.
  
  
  Attributes:
      points:
          Projected metrics for a series of bid modifier amounts.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.BidModifierSimulationPointList)
  ))
_sym_db.RegisterMessage(BidModifierSimulationPointList)

BidModifierSimulationPoint = _reflection.GeneratedProtocolMessageType('BidModifierSimulationPoint', (_message.Message,), dict(
  DESCRIPTOR = _BIDMODIFIERSIMULATIONPOINT,
  __module__ = 'google.ads.googleads_v1.proto.common.simulation_pb2'
  ,
  __doc__ = """Projected metrics for a specific bid modifier amount.
  
  
  Attributes:
      bid_modifier:
          The simulated bid modifier upon which projected metrics are
          based.
      biddable_conversions:
          Projected number of biddable conversions.
      biddable_conversions_value:
          Projected total value of biddable conversions.
      clicks:
          Projected number of clicks.
      cost_micros:
          Projected cost in micros.
      impressions:
          Projected number of impressions.
      top_slot_impressions:
          Projected number of top slot impressions.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.common.BidModifierSimulationPoint)
  ))
_sym_db.RegisterMessage(BidModifierSimulationPoint)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
