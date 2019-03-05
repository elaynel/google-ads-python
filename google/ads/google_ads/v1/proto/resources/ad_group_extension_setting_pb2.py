# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/ad_group_extension_setting.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.enums import extension_setting_device_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_extension__setting__device__pb2
from google.ads.google_ads.v1.proto.enums import extension_type_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_extension__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/ad_group_extension_setting.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\034AdGroupExtensionSettingProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\nHgoogle/ads/googleads_v1/proto/resources/ad_group_extension_setting.proto\x12!google.ads.googleads.v1.resources\x1a\x42google/ads/googleads_v1/proto/enums/extension_setting_device.proto\x1a\x38google/ads/googleads_v1/proto/enums/extension_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xd6\x02\n\x17\x41\x64GroupExtensionSetting\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12V\n\x0e\x65xtension_type\x18\x02 \x01(\x0e\x32>.google.ads.googleads.v1.enums.ExtensionTypeEnum.ExtensionType\x12.\n\x08\x61\x64_group\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14\x65xtension_feed_items\x18\x04 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x12`\n\x06\x64\x65vice\x18\x05 \x01(\x0e\x32P.google.ads.googleads.v1.enums.ExtensionSettingDeviceEnum.ExtensionSettingDeviceB\x89\x02\n%com.google.ads.googleads.v1.resourcesB\x1c\x41\x64GroupExtensionSettingProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_extension__setting__device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_extension__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPEXTENSIONSETTING = _descriptor.Descriptor(
  name='AdGroupExtensionSetting',
  full_name='google.ads.googleads.v1.resources.AdGroupExtensionSetting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.AdGroupExtensionSetting.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_type', full_name='google.ads.googleads.v1.resources.AdGroupExtensionSetting.extension_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v1.resources.AdGroupExtensionSetting.ad_group', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_feed_items', full_name='google.ads.googleads.v1.resources.AdGroupExtensionSetting.extension_feed_items', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v1.resources.AdGroupExtensionSetting.device', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=300,
  serialized_end=642,
)

_ADGROUPEXTENSIONSETTING.fields_by_name['extension_type'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_extension__type__pb2._EXTENSIONTYPEENUM_EXTENSIONTYPE
_ADGROUPEXTENSIONSETTING.fields_by_name['ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPEXTENSIONSETTING.fields_by_name['extension_feed_items'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPEXTENSIONSETTING.fields_by_name['device'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_extension__setting__device__pb2._EXTENSIONSETTINGDEVICEENUM_EXTENSIONSETTINGDEVICE
DESCRIPTOR.message_types_by_name['AdGroupExtensionSetting'] = _ADGROUPEXTENSIONSETTING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupExtensionSetting = _reflection.GeneratedProtocolMessageType('AdGroupExtensionSetting', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPEXTENSIONSETTING,
  __module__ = 'google.ads.googleads_v1.proto.resources.ad_group_extension_setting_pb2'
  ,
  __doc__ = """An ad group extension setting.
  
  
  Attributes:
      resource_name:
          The resource name of the ad group extension setting.
          AdGroupExtensionSetting resource names have the form:  ``custo
          mers/{customer_id}/adGroupExtensionSettings/{ad_group_id}~{ext
          ension_type}``
      extension_type:
          The extension type of the ad group extension setting.
      ad_group:
          The resource name of the ad group. The linked extension feed
          items will serve under this ad group. AdGroup resource names
          have the form:
          ``customers/{customer_id}/adGroups/{ad_group_id}``
      extension_feed_items:
          The resource names of the extension feed items to serve under
          the ad group. ExtensionFeedItem resource names have the form:
          ``customers/{customer_id}/extensionFeedItems/{feed_item_id}``
      device:
          The device for which the extensions will serve. Optional.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.AdGroupExtensionSetting)
  ))
_sym_db.RegisterMessage(AdGroupExtensionSetting)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
