# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rlibrary.proto\x12\x07service\"\x07\n\x05\x45mpty\"\x14\n\x04ISBN\x12\x0c\n\x04isbn\x18\x01 \x01(\t\"\xb4\x01\n\x04\x42ook\x12\x19\n\x02id\x18\x01 \x01(\x0b\x32\r.service.ISBN\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\"\n\x05genre\x18\x05 \x01(\x0e\x32\x13.service.Book.Genre\x12\x0c\n\x04year\x18\x04 \x01(\x05\"A\n\x05Genre\x12\x0c\n\x08suspense\x10\x00\x12\x0c\n\x08thriller\x10\x01\x12\x0e\n\nnonfiction\x10\x02\x12\x0c\n\x08selfhelp\x10\x03\"4\n\rInventoryItem\x12\x1b\n\x02\x62k\x18\x05 \x01(\x0b\x32\r.service.BookH\x00\x42\x06\n\x04\x62ook2l\n\x10InventoryService\x12-\n\nCreateBook\x12\r.service.Book\x1a\x0e.service.Empty\"\x00\x12)\n\x07GetBook\x12\r.service.ISBN\x1a\r.service.Book\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'library_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=26
  _EMPTY._serialized_end=33
  _ISBN._serialized_start=35
  _ISBN._serialized_end=55
  _BOOK._serialized_start=58
  _BOOK._serialized_end=238
  _BOOK_GENRE._serialized_start=173
  _BOOK_GENRE._serialized_end=238
  _INVENTORYITEM._serialized_start=240
  _INVENTORYITEM._serialized_end=292
  _INVENTORYSERVICE._serialized_start=294
  _INVENTORYSERVICE._serialized_end=402
# @@protoc_insertion_point(module_scope)
