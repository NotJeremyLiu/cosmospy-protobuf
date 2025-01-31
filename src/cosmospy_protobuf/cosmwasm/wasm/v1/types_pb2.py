# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1/types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63osmwasm/wasm/v1/types.proto\x12\x10\x63osmwasm.wasm.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\"V\n\x0f\x41\x63\x63\x65ssTypeParam\x12=\n\x05value\x18\x01 \x01(\x0e\x32\x1c.cosmwasm.wasm.v1.AccessTypeB\x10\xf2\xde\x1f\x0cyaml:\"value\":\x04\x98\xa0\x1f\x01\"\xab\x01\n\x0c\x41\x63\x63\x65ssConfig\x12G\n\npermission\x18\x01 \x01(\x0e\x32\x1c.cosmwasm.wasm.v1.AccessTypeB\x15\xf2\xde\x1f\x11yaml:\"permission\"\x12#\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"address\"\x12\'\n\taddresses\x18\x03 \x03(\tB\x14\xf2\xde\x1f\x10yaml:\"addresses\":\x04\x98\xa0\x1f\x01\"\xde\x01\n\x06Params\x12]\n\x12\x63ode_upload_access\x18\x01 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:\"code_upload_access\"\x12o\n\x1einstantiate_default_permission\x18\x02 \x01(\x0e\x32\x1c.cosmwasm.wasm.v1.AccessTypeB)\xf2\xde\x1f%yaml:\"instantiate_default_permission\":\x04\x98\xa0\x1f\x00\"|\n\x08\x43odeInfo\x12\x11\n\tcode_hash\x18\x01 \x01(\x0c\x12\x0f\n\x07\x63reator\x18\x02 \x01(\t\x12@\n\x12instantiate_config\x18\x05 \x01(\x0b\x32\x1e.cosmwasm.wasm.v1.AccessConfigB\x04\xc8\xde\x1f\x00J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05\"\xff\x01\n\x0c\x43ontractInfo\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\x0f\n\x07\x63reator\x18\x02 \x01(\t\x12\r\n\x05\x61\x64min\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\x12\x35\n\x07\x63reated\x18\x05 \x01(\x0b\x32$.cosmwasm.wasm.v1.AbsoluteTxPosition\x12\"\n\x0bibc_port_id\x18\x06 \x01(\tB\r\xe2\xde\x1f\tIBCPortID\x12\x42\n\textension\x18\x07 \x01(\x0b\x32\x14.google.protobuf.AnyB\x19\xca\xb4-\x15\x43ontractInfoExtension:\x04\xe8\xa0\x1f\x01\"\xda\x01\n\x18\x43ontractCodeHistoryEntry\x12\x45\n\toperation\x18\x01 \x01(\x0e\x32\x32.cosmwasm.wasm.v1.ContractCodeHistoryOperationType\x12\x1b\n\x07\x63ode_id\x18\x02 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\x35\n\x07updated\x18\x03 \x01(\x0b\x32$.cosmwasm.wasm.v1.AbsoluteTxPosition\x12#\n\x03msg\x18\x04 \x01(\x0c\x42\x16\xfa\xde\x1f\x12RawContractMessage\"<\n\x12\x41\x62soluteTxPosition\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x04\x12\x10\n\x08tx_index\x18\x02 \x01(\x04\"]\n\x05Model\x12\x45\n\x03key\x18\x01 \x01(\x0c\x42\x38\xfa\xde\x1f\x34github.com/tendermint/tendermint/libs/bytes.HexBytes\x12\r\n\x05value\x18\x02 \x01(\x0c*\xa9\x02\n\nAccessType\x12\x36\n\x17\x41\x43\x43\x45SS_TYPE_UNSPECIFIED\x10\x00\x1a\x19\x8a\x9d \x15\x41\x63\x63\x65ssTypeUnspecified\x12,\n\x12\x41\x43\x43\x45SS_TYPE_NOBODY\x10\x01\x1a\x14\x8a\x9d \x10\x41\x63\x63\x65ssTypeNobody\x12\x37\n\x18\x41\x43\x43\x45SS_TYPE_ONLY_ADDRESS\x10\x02\x1a\x19\x8a\x9d \x15\x41\x63\x63\x65ssTypeOnlyAddress\x12\x32\n\x15\x41\x43\x43\x45SS_TYPE_EVERYBODY\x10\x03\x1a\x17\x8a\x9d \x13\x41\x63\x63\x65ssTypeEverybody\x12>\n\x1c\x41\x43\x43\x45SS_TYPE_ANY_OF_ADDRESSES\x10\x04\x1a\x1c\x8a\x9d \x18\x41\x63\x63\x65ssTypeAnyOfAddresses\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x00*\xa6\x03\n ContractCodeHistoryOperationType\x12\x65\n0CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED\x10\x00\x1a/\x8a\x9d +ContractCodeHistoryOperationTypeUnspecified\x12W\n)CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT\x10\x01\x1a(\x8a\x9d $ContractCodeHistoryOperationTypeInit\x12]\n,CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE\x10\x02\x1a+\x8a\x9d \'ContractCodeHistoryOperationTypeMigrate\x12]\n,CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS\x10\x03\x1a+\x8a\x9d \'ContractCodeHistoryOperationTypeGenesis\x1a\x04\x88\xa3\x1e\x00\x42\x30Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\xa8\xe2\x1e\x01\x62\x06proto3')

_ACCESSTYPE = DESCRIPTOR.enum_types_by_name['AccessType']
AccessType = enum_type_wrapper.EnumTypeWrapper(_ACCESSTYPE)
_CONTRACTCODEHISTORYOPERATIONTYPE = DESCRIPTOR.enum_types_by_name['ContractCodeHistoryOperationType']
ContractCodeHistoryOperationType = enum_type_wrapper.EnumTypeWrapper(_CONTRACTCODEHISTORYOPERATIONTYPE)
ACCESS_TYPE_UNSPECIFIED = 0
ACCESS_TYPE_NOBODY = 1
ACCESS_TYPE_ONLY_ADDRESS = 2
ACCESS_TYPE_EVERYBODY = 3
ACCESS_TYPE_ANY_OF_ADDRESSES = 4
CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED = 0
CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT = 1
CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE = 2
CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS = 3


_ACCESSTYPEPARAM = DESCRIPTOR.message_types_by_name['AccessTypeParam']
_ACCESSCONFIG = DESCRIPTOR.message_types_by_name['AccessConfig']
_PARAMS = DESCRIPTOR.message_types_by_name['Params']
_CODEINFO = DESCRIPTOR.message_types_by_name['CodeInfo']
_CONTRACTINFO = DESCRIPTOR.message_types_by_name['ContractInfo']
_CONTRACTCODEHISTORYENTRY = DESCRIPTOR.message_types_by_name['ContractCodeHistoryEntry']
_ABSOLUTETXPOSITION = DESCRIPTOR.message_types_by_name['AbsoluteTxPosition']
_MODEL = DESCRIPTOR.message_types_by_name['Model']
AccessTypeParam = _reflection.GeneratedProtocolMessageType('AccessTypeParam', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSTYPEPARAM,
  '__module__' : 'cosmwasm.wasm.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.AccessTypeParam)
  })
_sym_db.RegisterMessage(AccessTypeParam)

AccessConfig = _reflection.GeneratedProtocolMessageType('AccessConfig', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSCONFIG,
  '__module__' : 'cosmwasm.wasm.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.AccessConfig)
  })
_sym_db.RegisterMessage(AccessConfig)

Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'cosmwasm.wasm.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.Params)
  })
_sym_db.RegisterMessage(Params)

CodeInfo = _reflection.GeneratedProtocolMessageType('CodeInfo', (_message.Message,), {
  'DESCRIPTOR' : _CODEINFO,
  '__module__' : 'cosmwasm.wasm.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.CodeInfo)
  })
_sym_db.RegisterMessage(CodeInfo)

ContractInfo = _reflection.GeneratedProtocolMessageType('ContractInfo', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACTINFO,
  '__module__' : 'cosmwasm.wasm.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.ContractInfo)
  })
_sym_db.RegisterMessage(ContractInfo)

ContractCodeHistoryEntry = _reflection.GeneratedProtocolMessageType('ContractCodeHistoryEntry', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACTCODEHISTORYENTRY,
  '__module__' : 'cosmwasm.wasm.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.ContractCodeHistoryEntry)
  })
_sym_db.RegisterMessage(ContractCodeHistoryEntry)

AbsoluteTxPosition = _reflection.GeneratedProtocolMessageType('AbsoluteTxPosition', (_message.Message,), {
  'DESCRIPTOR' : _ABSOLUTETXPOSITION,
  '__module__' : 'cosmwasm.wasm.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.AbsoluteTxPosition)
  })
_sym_db.RegisterMessage(AbsoluteTxPosition)

Model = _reflection.GeneratedProtocolMessageType('Model', (_message.Message,), {
  'DESCRIPTOR' : _MODEL,
  '__module__' : 'cosmwasm.wasm.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1.Model)
  })
_sym_db.RegisterMessage(Model)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/CosmWasm/wasmd/x/wasm/types\310\341\036\000\250\342\036\001'
  _ACCESSTYPE._options = None
  _ACCESSTYPE._serialized_options = b'\210\243\036\000\250\244\036\000'
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_UNSPECIFIED"]._options = None
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_UNSPECIFIED"]._serialized_options = b'\212\235 \025AccessTypeUnspecified'
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_NOBODY"]._options = None
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_NOBODY"]._serialized_options = b'\212\235 \020AccessTypeNobody'
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_ONLY_ADDRESS"]._options = None
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_ONLY_ADDRESS"]._serialized_options = b'\212\235 \025AccessTypeOnlyAddress'
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_EVERYBODY"]._options = None
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_EVERYBODY"]._serialized_options = b'\212\235 \023AccessTypeEverybody'
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_ANY_OF_ADDRESSES"]._options = None
  _ACCESSTYPE.values_by_name["ACCESS_TYPE_ANY_OF_ADDRESSES"]._serialized_options = b'\212\235 \030AccessTypeAnyOfAddresses'
  _CONTRACTCODEHISTORYOPERATIONTYPE._options = None
  _CONTRACTCODEHISTORYOPERATIONTYPE._serialized_options = b'\210\243\036\000'
  _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name["CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED"]._options = None
  _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name["CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED"]._serialized_options = b'\212\235 +ContractCodeHistoryOperationTypeUnspecified'
  _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name["CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT"]._options = None
  _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name["CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT"]._serialized_options = b'\212\235 $ContractCodeHistoryOperationTypeInit'
  _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name["CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE"]._options = None
  _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name["CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE"]._serialized_options = b'\212\235 \'ContractCodeHistoryOperationTypeMigrate'
  _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name["CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS"]._options = None
  _CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name["CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS"]._serialized_options = b'\212\235 \'ContractCodeHistoryOperationTypeGenesis'
  _ACCESSTYPEPARAM.fields_by_name['value']._options = None
  _ACCESSTYPEPARAM.fields_by_name['value']._serialized_options = b'\362\336\037\014yaml:\"value\"'
  _ACCESSTYPEPARAM._options = None
  _ACCESSTYPEPARAM._serialized_options = b'\230\240\037\001'
  _ACCESSCONFIG.fields_by_name['permission']._options = None
  _ACCESSCONFIG.fields_by_name['permission']._serialized_options = b'\362\336\037\021yaml:\"permission\"'
  _ACCESSCONFIG.fields_by_name['address']._options = None
  _ACCESSCONFIG.fields_by_name['address']._serialized_options = b'\362\336\037\016yaml:\"address\"'
  _ACCESSCONFIG.fields_by_name['addresses']._options = None
  _ACCESSCONFIG.fields_by_name['addresses']._serialized_options = b'\362\336\037\020yaml:\"addresses\"'
  _ACCESSCONFIG._options = None
  _ACCESSCONFIG._serialized_options = b'\230\240\037\001'
  _PARAMS.fields_by_name['code_upload_access']._options = None
  _PARAMS.fields_by_name['code_upload_access']._serialized_options = b'\310\336\037\000\362\336\037\031yaml:\"code_upload_access\"'
  _PARAMS.fields_by_name['instantiate_default_permission']._options = None
  _PARAMS.fields_by_name['instantiate_default_permission']._serialized_options = b'\362\336\037%yaml:\"instantiate_default_permission\"'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\230\240\037\000'
  _CODEINFO.fields_by_name['instantiate_config']._options = None
  _CODEINFO.fields_by_name['instantiate_config']._serialized_options = b'\310\336\037\000'
  _CONTRACTINFO.fields_by_name['code_id']._options = None
  _CONTRACTINFO.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _CONTRACTINFO.fields_by_name['ibc_port_id']._options = None
  _CONTRACTINFO.fields_by_name['ibc_port_id']._serialized_options = b'\342\336\037\tIBCPortID'
  _CONTRACTINFO.fields_by_name['extension']._options = None
  _CONTRACTINFO.fields_by_name['extension']._serialized_options = b'\312\264-\025ContractInfoExtension'
  _CONTRACTINFO._options = None
  _CONTRACTINFO._serialized_options = b'\350\240\037\001'
  _CONTRACTCODEHISTORYENTRY.fields_by_name['code_id']._options = None
  _CONTRACTCODEHISTORYENTRY.fields_by_name['code_id']._serialized_options = b'\342\336\037\006CodeID'
  _CONTRACTCODEHISTORYENTRY.fields_by_name['msg']._options = None
  _CONTRACTCODEHISTORYENTRY.fields_by_name['msg']._serialized_options = b'\372\336\037\022RawContractMessage'
  _MODEL.fields_by_name['key']._options = None
  _MODEL.fields_by_name['key']._serialized_options = b'\372\336\0374github.com/tendermint/tendermint/libs/bytes.HexBytes'
  _ACCESSTYPE._serialized_start=1376
  _ACCESSTYPE._serialized_end=1673
  _CONTRACTCODEHISTORYOPERATIONTYPE._serialized_start=1676
  _CONTRACTCODEHISTORYOPERATIONTYPE._serialized_end=2098
  _ACCESSTYPEPARAM._serialized_start=126
  _ACCESSTYPEPARAM._serialized_end=212
  _ACCESSCONFIG._serialized_start=215
  _ACCESSCONFIG._serialized_end=386
  _PARAMS._serialized_start=389
  _PARAMS._serialized_end=611
  _CODEINFO._serialized_start=613
  _CODEINFO._serialized_end=737
  _CONTRACTINFO._serialized_start=740
  _CONTRACTINFO._serialized_end=995
  _CONTRACTCODEHISTORYENTRY._serialized_start=998
  _CONTRACTCODEHISTORYENTRY._serialized_end=1216
  _ABSOLUTETXPOSITION._serialized_start=1218
  _ABSOLUTETXPOSITION._serialized_end=1278
  _MODEL._serialized_start=1280
  _MODEL._serialized_end=1373
# @@protoc_insertion_point(module_scope)
