# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/bank/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.bank.v1beta1 import bank_pb2 as cosmos_dot_bank_dot_v1beta1_dot_bank__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63osmos/bank/v1beta1/query.proto\x12\x13\x63osmos.bank.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1e\x63osmos/bank/v1beta1/bank.proto\"?\n\x13QueryBalanceRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05\x64\x65nom\x18\x02 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"B\n\x14QueryBalanceResponse\x12*\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.Coin\"p\n\x17QueryAllBalancesRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb6\x01\n\x18QueryAllBalancesResponse\x12]\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"v\n\x1dQuerySpendableBalancesRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xbc\x01\n\x1eQuerySpendableBalancesResponse\x12]\n\x08\x62\x61lances\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"_\n\x17QueryTotalSupplyRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\xb4\x01\n\x18QueryTotalSupplyResponse\x12[\n\x06supply\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"%\n\x14QuerySupplyOfRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"H\n\x15QuerySupplyOfResponse\x12/\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\"\x14\n\x12QueryParamsRequest\"H\n\x13QueryParamsResponse\x12\x31\n\x06params\x18\x01 \x01(\x0b\x32\x1b.cosmos.bank.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\"X\n\x1aQueryDenomsMetadataRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x92\x01\n\x1bQueryDenomsMetadataResponse\x12\x36\n\tmetadatas\x18\x01 \x03(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"*\n\x19QueryDenomMetadataRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\"S\n\x1aQueryDenomMetadataResponse\x12\x35\n\x08metadata\x18\x01 \x01(\x0b\x32\x1d.cosmos.bank.v1beta1.MetadataB\x04\xc8\xde\x1f\x00\x32\xed\t\n\x05Query\x12\x98\x01\n\x07\x42\x61lance\x12(.cosmos.bank.v1beta1.QueryBalanceRequest\x1a).cosmos.bank.v1beta1.QueryBalanceResponse\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/cosmos/bank/v1beta1/balances/{address}/by_denom\x12\x9b\x01\n\x0b\x41llBalances\x12,.cosmos.bank.v1beta1.QueryAllBalancesRequest\x1a-.cosmos.bank.v1beta1.QueryAllBalancesResponse\"/\x82\xd3\xe4\x93\x02)\x12\'/cosmos/bank/v1beta1/balances/{address}\x12\xb7\x01\n\x11SpendableBalances\x12\x32.cosmos.bank.v1beta1.QuerySpendableBalancesRequest\x1a\x33.cosmos.bank.v1beta1.QuerySpendableBalancesResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/cosmos/bank/v1beta1/spendable_balances/{address}\x12\x8f\x01\n\x0bTotalSupply\x12,.cosmos.bank.v1beta1.QueryTotalSupplyRequest\x1a-.cosmos.bank.v1beta1.QueryTotalSupplyResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/supply\x12\x8e\x01\n\x08SupplyOf\x12).cosmos.bank.v1beta1.QuerySupplyOfRequest\x1a*.cosmos.bank.v1beta1.QuerySupplyOfResponse\"+\x82\xd3\xe4\x93\x02%\x12#/cosmos/bank/v1beta1/supply/{denom}\x12\x80\x01\n\x06Params\x12\'.cosmos.bank.v1beta1.QueryParamsRequest\x1a(.cosmos.bank.v1beta1.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/bank/v1beta1/params\x12\xa6\x01\n\rDenomMetadata\x12..cosmos.bank.v1beta1.QueryDenomMetadataRequest\x1a/.cosmos.bank.v1beta1.QueryDenomMetadataResponse\"4\x82\xd3\xe4\x93\x02.\x12,/cosmos/bank/v1beta1/denoms_metadata/{denom}\x12\xa1\x01\n\x0e\x44\x65nomsMetadata\x12/.cosmos.bank.v1beta1.QueryDenomsMetadataRequest\x1a\x30.cosmos.bank.v1beta1.QueryDenomsMetadataResponse\",\x82\xd3\xe4\x93\x02&\x12$/cosmos/bank/v1beta1/denoms_metadataB+Z)github.com/cosmos/cosmos-sdk/x/bank/typesb\x06proto3')



_QUERYBALANCEREQUEST = DESCRIPTOR.message_types_by_name['QueryBalanceRequest']
_QUERYBALANCERESPONSE = DESCRIPTOR.message_types_by_name['QueryBalanceResponse']
_QUERYALLBALANCESREQUEST = DESCRIPTOR.message_types_by_name['QueryAllBalancesRequest']
_QUERYALLBALANCESRESPONSE = DESCRIPTOR.message_types_by_name['QueryAllBalancesResponse']
_QUERYSPENDABLEBALANCESREQUEST = DESCRIPTOR.message_types_by_name['QuerySpendableBalancesRequest']
_QUERYSPENDABLEBALANCESRESPONSE = DESCRIPTOR.message_types_by_name['QuerySpendableBalancesResponse']
_QUERYTOTALSUPPLYREQUEST = DESCRIPTOR.message_types_by_name['QueryTotalSupplyRequest']
_QUERYTOTALSUPPLYRESPONSE = DESCRIPTOR.message_types_by_name['QueryTotalSupplyResponse']
_QUERYSUPPLYOFREQUEST = DESCRIPTOR.message_types_by_name['QuerySupplyOfRequest']
_QUERYSUPPLYOFRESPONSE = DESCRIPTOR.message_types_by_name['QuerySupplyOfResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYDENOMSMETADATAREQUEST = DESCRIPTOR.message_types_by_name['QueryDenomsMetadataRequest']
_QUERYDENOMSMETADATARESPONSE = DESCRIPTOR.message_types_by_name['QueryDenomsMetadataResponse']
_QUERYDENOMMETADATAREQUEST = DESCRIPTOR.message_types_by_name['QueryDenomMetadataRequest']
_QUERYDENOMMETADATARESPONSE = DESCRIPTOR.message_types_by_name['QueryDenomMetadataResponse']
QueryBalanceRequest = _reflection.GeneratedProtocolMessageType('QueryBalanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBALANCEREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryBalanceRequest)
  })
_sym_db.RegisterMessage(QueryBalanceRequest)

QueryBalanceResponse = _reflection.GeneratedProtocolMessageType('QueryBalanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYBALANCERESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryBalanceResponse)
  })
_sym_db.RegisterMessage(QueryBalanceResponse)

QueryAllBalancesRequest = _reflection.GeneratedProtocolMessageType('QueryAllBalancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLBALANCESREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryAllBalancesRequest)
  })
_sym_db.RegisterMessage(QueryAllBalancesRequest)

QueryAllBalancesResponse = _reflection.GeneratedProtocolMessageType('QueryAllBalancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYALLBALANCESRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryAllBalancesResponse)
  })
_sym_db.RegisterMessage(QueryAllBalancesResponse)

QuerySpendableBalancesRequest = _reflection.GeneratedProtocolMessageType('QuerySpendableBalancesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSPENDABLEBALANCESREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QuerySpendableBalancesRequest)
  })
_sym_db.RegisterMessage(QuerySpendableBalancesRequest)

QuerySpendableBalancesResponse = _reflection.GeneratedProtocolMessageType('QuerySpendableBalancesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSPENDABLEBALANCESRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QuerySpendableBalancesResponse)
  })
_sym_db.RegisterMessage(QuerySpendableBalancesResponse)

QueryTotalSupplyRequest = _reflection.GeneratedProtocolMessageType('QueryTotalSupplyRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALSUPPLYREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryTotalSupplyRequest)
  })
_sym_db.RegisterMessage(QueryTotalSupplyRequest)

QueryTotalSupplyResponse = _reflection.GeneratedProtocolMessageType('QueryTotalSupplyResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALSUPPLYRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryTotalSupplyResponse)
  })
_sym_db.RegisterMessage(QueryTotalSupplyResponse)

QuerySupplyOfRequest = _reflection.GeneratedProtocolMessageType('QuerySupplyOfRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSUPPLYOFREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QuerySupplyOfRequest)
  })
_sym_db.RegisterMessage(QuerySupplyOfRequest)

QuerySupplyOfResponse = _reflection.GeneratedProtocolMessageType('QuerySupplyOfResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSUPPLYOFRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QuerySupplyOfResponse)
  })
_sym_db.RegisterMessage(QuerySupplyOfResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryDenomsMetadataRequest = _reflection.GeneratedProtocolMessageType('QueryDenomsMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMSMETADATAREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryDenomsMetadataRequest)
  })
_sym_db.RegisterMessage(QueryDenomsMetadataRequest)

QueryDenomsMetadataResponse = _reflection.GeneratedProtocolMessageType('QueryDenomsMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMSMETADATARESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryDenomsMetadataResponse)
  })
_sym_db.RegisterMessage(QueryDenomsMetadataResponse)

QueryDenomMetadataRequest = _reflection.GeneratedProtocolMessageType('QueryDenomMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMMETADATAREQUEST,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryDenomMetadataRequest)
  })
_sym_db.RegisterMessage(QueryDenomMetadataRequest)

QueryDenomMetadataResponse = _reflection.GeneratedProtocolMessageType('QueryDenomMetadataResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDENOMMETADATARESPONSE,
  '__module__' : 'cosmos.bank.v1beta1.query_pb2'
  # @@protoc_insertion_point(class_scope:cosmos.bank.v1beta1.QueryDenomMetadataResponse)
  })
_sym_db.RegisterMessage(QueryDenomMetadataResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/bank/types'
  _QUERYBALANCEREQUEST._options = None
  _QUERYBALANCEREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYALLBALANCESREQUEST._options = None
  _QUERYALLBALANCESREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._options = None
  _QUERYALLBALANCESRESPONSE.fields_by_name['balances']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYSPENDABLEBALANCESREQUEST._options = None
  _QUERYSPENDABLEBALANCESREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYSPENDABLEBALANCESRESPONSE.fields_by_name['balances']._options = None
  _QUERYSPENDABLEBALANCESRESPONSE.fields_by_name['balances']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYTOTALSUPPLYREQUEST._options = None
  _QUERYTOTALSUPPLYREQUEST._serialized_options = b'\350\240\037\000\210\240\037\000'
  _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._options = None
  _QUERYTOTALSUPPLYRESPONSE.fields_by_name['supply']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._options = None
  _QUERYSUPPLYOFRESPONSE.fields_by_name['amount']._serialized_options = b'\310\336\037\000'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._options = None
  _QUERYDENOMSMETADATARESPONSE.fields_by_name['metadatas']._serialized_options = b'\310\336\037\000'
  _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._options = None
  _QUERYDENOMMETADATARESPONSE.fields_by_name['metadata']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['Balance']._options = None
  _QUERY.methods_by_name['Balance']._serialized_options = b'\202\323\344\223\0022\0220/cosmos/bank/v1beta1/balances/{address}/by_denom'
  _QUERY.methods_by_name['AllBalances']._options = None
  _QUERY.methods_by_name['AllBalances']._serialized_options = b'\202\323\344\223\002)\022\'/cosmos/bank/v1beta1/balances/{address}'
  _QUERY.methods_by_name['SpendableBalances']._options = None
  _QUERY.methods_by_name['SpendableBalances']._serialized_options = b'\202\323\344\223\0023\0221/cosmos/bank/v1beta1/spendable_balances/{address}'
  _QUERY.methods_by_name['TotalSupply']._options = None
  _QUERY.methods_by_name['TotalSupply']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/supply'
  _QUERY.methods_by_name['SupplyOf']._options = None
  _QUERY.methods_by_name['SupplyOf']._serialized_options = b'\202\323\344\223\002%\022#/cosmos/bank/v1beta1/supply/{denom}'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/bank/v1beta1/params'
  _QUERY.methods_by_name['DenomMetadata']._options = None
  _QUERY.methods_by_name['DenomMetadata']._serialized_options = b'\202\323\344\223\002.\022,/cosmos/bank/v1beta1/denoms_metadata/{denom}'
  _QUERY.methods_by_name['DenomsMetadata']._options = None
  _QUERY.methods_by_name['DenomsMetadata']._serialized_options = b'\202\323\344\223\002&\022$/cosmos/bank/v1beta1/denoms_metadata'
  _QUERYBALANCEREQUEST._serialized_start=216
  _QUERYBALANCEREQUEST._serialized_end=279
  _QUERYBALANCERESPONSE._serialized_start=281
  _QUERYBALANCERESPONSE._serialized_end=347
  _QUERYALLBALANCESREQUEST._serialized_start=349
  _QUERYALLBALANCESREQUEST._serialized_end=461
  _QUERYALLBALANCESRESPONSE._serialized_start=464
  _QUERYALLBALANCESRESPONSE._serialized_end=646
  _QUERYSPENDABLEBALANCESREQUEST._serialized_start=648
  _QUERYSPENDABLEBALANCESREQUEST._serialized_end=766
  _QUERYSPENDABLEBALANCESRESPONSE._serialized_start=769
  _QUERYSPENDABLEBALANCESRESPONSE._serialized_end=957
  _QUERYTOTALSUPPLYREQUEST._serialized_start=959
  _QUERYTOTALSUPPLYREQUEST._serialized_end=1054
  _QUERYTOTALSUPPLYRESPONSE._serialized_start=1057
  _QUERYTOTALSUPPLYRESPONSE._serialized_end=1237
  _QUERYSUPPLYOFREQUEST._serialized_start=1239
  _QUERYSUPPLYOFREQUEST._serialized_end=1276
  _QUERYSUPPLYOFRESPONSE._serialized_start=1278
  _QUERYSUPPLYOFRESPONSE._serialized_end=1350
  _QUERYPARAMSREQUEST._serialized_start=1352
  _QUERYPARAMSREQUEST._serialized_end=1372
  _QUERYPARAMSRESPONSE._serialized_start=1374
  _QUERYPARAMSRESPONSE._serialized_end=1446
  _QUERYDENOMSMETADATAREQUEST._serialized_start=1448
  _QUERYDENOMSMETADATAREQUEST._serialized_end=1536
  _QUERYDENOMSMETADATARESPONSE._serialized_start=1539
  _QUERYDENOMSMETADATARESPONSE._serialized_end=1685
  _QUERYDENOMMETADATAREQUEST._serialized_start=1687
  _QUERYDENOMMETADATAREQUEST._serialized_end=1729
  _QUERYDENOMMETADATARESPONSE._serialized_start=1731
  _QUERYDENOMMETADATARESPONSE._serialized_end=1814
  _QUERY._serialized_start=1817
  _QUERY._serialized_end=3078
# @@protoc_insertion_point(module_scope)
