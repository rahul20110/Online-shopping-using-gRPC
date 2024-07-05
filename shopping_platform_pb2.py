# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shopping_platform.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17shopping_platform.proto\x12\x11shopping_platform\"\"\n\x12\x43heckSellerRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"%\n\x13\x43heckSellerResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"6\n\x15RegisterSellerRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\"1\n\x0eSellerResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07item_id\x18\x02 \x01(\x05\"\xb1\x01\n\x0fSellItemRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1b.shopping_platform.Category\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\x05\x12\x16\n\x0eseller_address\x18\x06 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x07 \x01(\t\"r\n\x11UpdateItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x05\x12\x10\n\x08quantity\x18\x03 \x01(\x05\x12\x16\n\x0eseller_address\x18\x04 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x05 \x01(\t\"Q\n\x11\x44\x65leteItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x16\n\x0eseller_address\x18\x02 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x03 \x01(\t\"B\n\x13\x44isplayItemsRequest\x12\x16\n\x0eseller_address\x18\x01 \x01(\t\x12\x13\n\x0bseller_uuid\x18\x02 \x01(\t\">\n\x14\x44isplayItemsResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.shopping_platform.Item\"\xc2\x01\n\x04Item\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05price\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12-\n\x08\x63\x61tegory\x18\x04 \x01(\x0e\x32\x1b.shopping_platform.Category\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x10\n\x08quantity\x18\x06 \x01(\x05\x12\x0e\n\x06rating\x18\x07 \x01(\x01\x12\x16\n\x0eseller_address\x18\x08 \x01(\t\x12\x13\n\x0bseller_uuid\x18\t \x01(\t\"P\n\x11SearchItemRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12-\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1b.shopping_platform.Category\"<\n\x12SearchItemResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.shopping_platform.Item\"J\n\x0e\x42uyItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x15\n\rbuyer_address\x18\x03 \x01(\t\"\x1f\n\rBuyerResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"P\n\x14\x41\x64\x64ToWishlistRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x15\n\rbuyer_address\x18\x02 \x01(\t\x12\x10\n\x08\x62uyer_id\x18\x03 \x01(\t\"I\n\x0fRateItemRequest\x12\x0f\n\x07item_id\x18\x01 \x01(\x05\x12\x15\n\rbuyer_address\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05\"9\n\x10ItemNotification\x12%\n\x04item\x18\x01 \x01(\x0b\x32\x17.shopping_platform.Item\"/\n\x05\x45mpty\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.shopping_platform.Item*4\n\x08\x43\x61tegory\x12\x0f\n\x0b\x45LECTRONICS\x10\x00\x12\x0b\n\x07\x46\x41SHION\x10\x01\x12\n\n\x06OTHERS\x10\x02\x32\xf7\x04\n\rSellerService\x12V\n\x05Login\x12%.shopping_platform.CheckSellerRequest\x1a&.shopping_platform.CheckSellerResponse\x12]\n\x0eRegisterSeller\x12(.shopping_platform.RegisterSellerRequest\x1a!.shopping_platform.SellerResponse\x12Q\n\x08SellItem\x12\".shopping_platform.SellItemRequest\x1a!.shopping_platform.SellerResponse\x12U\n\nUpdateItem\x12$.shopping_platform.UpdateItemRequest\x1a!.shopping_platform.SellerResponse\x12U\n\nDeleteItem\x12$.shopping_platform.DeleteItemRequest\x1a!.shopping_platform.SellerResponse\x12_\n\x0c\x44isplayItems\x12&.shopping_platform.DisplayItemsRequest\x1a\'.shopping_platform.DisplayItemsResponse\x12M\n\x0cNotifySeller\x12#.shopping_platform.ItemNotification\x1a\x18.shopping_platform.Empty2\xb5\x03\n\x0c\x42uyerService\x12Y\n\nSearchItem\x12$.shopping_platform.SearchItemRequest\x1a%.shopping_platform.SearchItemResponse\x12N\n\x07\x42uyItem\x12!.shopping_platform.BuyItemRequest\x1a .shopping_platform.BuyerResponse\x12Z\n\rAddToWishlist\x12\'.shopping_platform.AddToWishlistRequest\x1a .shopping_platform.BuyerResponse\x12P\n\x08RateItem\x12\".shopping_platform.RateItemRequest\x1a .shopping_platform.BuyerResponse\x12L\n\x0bNotifyBuyer\x12#.shopping_platform.ItemNotification\x1a\x18.shopping_platform.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'shopping_platform_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CATEGORY']._serialized_start=1454
  _globals['_CATEGORY']._serialized_end=1506
  _globals['_CHECKSELLERREQUEST']._serialized_start=46
  _globals['_CHECKSELLERREQUEST']._serialized_end=80
  _globals['_CHECKSELLERRESPONSE']._serialized_start=82
  _globals['_CHECKSELLERRESPONSE']._serialized_end=119
  _globals['_REGISTERSELLERREQUEST']._serialized_start=121
  _globals['_REGISTERSELLERREQUEST']._serialized_end=175
  _globals['_SELLERRESPONSE']._serialized_start=177
  _globals['_SELLERRESPONSE']._serialized_end=226
  _globals['_SELLITEMREQUEST']._serialized_start=229
  _globals['_SELLITEMREQUEST']._serialized_end=406
  _globals['_UPDATEITEMREQUEST']._serialized_start=408
  _globals['_UPDATEITEMREQUEST']._serialized_end=522
  _globals['_DELETEITEMREQUEST']._serialized_start=524
  _globals['_DELETEITEMREQUEST']._serialized_end=605
  _globals['_DISPLAYITEMSREQUEST']._serialized_start=607
  _globals['_DISPLAYITEMSREQUEST']._serialized_end=673
  _globals['_DISPLAYITEMSRESPONSE']._serialized_start=675
  _globals['_DISPLAYITEMSRESPONSE']._serialized_end=737
  _globals['_ITEM']._serialized_start=740
  _globals['_ITEM']._serialized_end=934
  _globals['_SEARCHITEMREQUEST']._serialized_start=936
  _globals['_SEARCHITEMREQUEST']._serialized_end=1016
  _globals['_SEARCHITEMRESPONSE']._serialized_start=1018
  _globals['_SEARCHITEMRESPONSE']._serialized_end=1078
  _globals['_BUYITEMREQUEST']._serialized_start=1080
  _globals['_BUYITEMREQUEST']._serialized_end=1154
  _globals['_BUYERRESPONSE']._serialized_start=1156
  _globals['_BUYERRESPONSE']._serialized_end=1187
  _globals['_ADDTOWISHLISTREQUEST']._serialized_start=1189
  _globals['_ADDTOWISHLISTREQUEST']._serialized_end=1269
  _globals['_RATEITEMREQUEST']._serialized_start=1271
  _globals['_RATEITEMREQUEST']._serialized_end=1344
  _globals['_ITEMNOTIFICATION']._serialized_start=1346
  _globals['_ITEMNOTIFICATION']._serialized_end=1403
  _globals['_EMPTY']._serialized_start=1405
  _globals['_EMPTY']._serialized_end=1452
  _globals['_SELLERSERVICE']._serialized_start=1509
  _globals['_SELLERSERVICE']._serialized_end=2140
  _globals['_BUYERSERVICE']._serialized_start=2143
  _globals['_BUYERSERVICE']._serialized_end=2580
# @@protoc_insertion_point(module_scope)
