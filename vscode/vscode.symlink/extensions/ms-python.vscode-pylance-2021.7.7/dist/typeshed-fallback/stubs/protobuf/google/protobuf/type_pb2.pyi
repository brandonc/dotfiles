"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.source_context_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Syntax(metaclass=_Syntax):
    V = typing.NewType('V', builtins.int)

global___Syntax = Syntax

SYNTAX_PROTO2 = Syntax.V(0)
SYNTAX_PROTO3 = Syntax.V(1)

class _Syntax(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Syntax.V], builtins.type):  # type: ignore
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    SYNTAX_PROTO2 = Syntax.V(0)
    SYNTAX_PROTO3 = Syntax.V(1)

class Type(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    ONEOFS_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    SOURCE_CONTEXT_FIELD_NUMBER: builtins.int
    SYNTAX_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    @property
    def oneofs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    syntax: global___Syntax.V = ...

    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Field]: ...

    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Option]: ...

    @property
    def source_context(self) -> google.protobuf.source_context_pb2.SourceContext: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        fields : typing.Optional[typing.Iterable[global___Field]] = ...,
        oneofs : typing.Optional[typing.Iterable[typing.Text]] = ...,
        options : typing.Optional[typing.Iterable[global___Option]] = ...,
        source_context : typing.Optional[google.protobuf.source_context_pb2.SourceContext] = ...,
        syntax : global___Syntax.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"source_context",b"source_context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"fields",b"fields",u"name",b"name",u"oneofs",b"oneofs",u"options",b"options",u"source_context",b"source_context",u"syntax",b"syntax"]) -> None: ...
global___Type = Type

class Field(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Kind(metaclass=_Kind):
        V = typing.NewType('V', builtins.int)

    TYPE_UNKNOWN = Field.Kind.V(0)
    TYPE_DOUBLE = Field.Kind.V(1)
    TYPE_FLOAT = Field.Kind.V(2)
    TYPE_INT64 = Field.Kind.V(3)
    TYPE_UINT64 = Field.Kind.V(4)
    TYPE_INT32 = Field.Kind.V(5)
    TYPE_FIXED64 = Field.Kind.V(6)
    TYPE_FIXED32 = Field.Kind.V(7)
    TYPE_BOOL = Field.Kind.V(8)
    TYPE_STRING = Field.Kind.V(9)
    TYPE_GROUP = Field.Kind.V(10)
    TYPE_MESSAGE = Field.Kind.V(11)
    TYPE_BYTES = Field.Kind.V(12)
    TYPE_UINT32 = Field.Kind.V(13)
    TYPE_ENUM = Field.Kind.V(14)
    TYPE_SFIXED32 = Field.Kind.V(15)
    TYPE_SFIXED64 = Field.Kind.V(16)
    TYPE_SINT32 = Field.Kind.V(17)
    TYPE_SINT64 = Field.Kind.V(18)

    class _Kind(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Kind.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TYPE_UNKNOWN = Field.Kind.V(0)
        TYPE_DOUBLE = Field.Kind.V(1)
        TYPE_FLOAT = Field.Kind.V(2)
        TYPE_INT64 = Field.Kind.V(3)
        TYPE_UINT64 = Field.Kind.V(4)
        TYPE_INT32 = Field.Kind.V(5)
        TYPE_FIXED64 = Field.Kind.V(6)
        TYPE_FIXED32 = Field.Kind.V(7)
        TYPE_BOOL = Field.Kind.V(8)
        TYPE_STRING = Field.Kind.V(9)
        TYPE_GROUP = Field.Kind.V(10)
        TYPE_MESSAGE = Field.Kind.V(11)
        TYPE_BYTES = Field.Kind.V(12)
        TYPE_UINT32 = Field.Kind.V(13)
        TYPE_ENUM = Field.Kind.V(14)
        TYPE_SFIXED32 = Field.Kind.V(15)
        TYPE_SFIXED64 = Field.Kind.V(16)
        TYPE_SINT32 = Field.Kind.V(17)
        TYPE_SINT64 = Field.Kind.V(18)

    class Cardinality(metaclass=_Cardinality):
        V = typing.NewType('V', builtins.int)

    CARDINALITY_UNKNOWN = Field.Cardinality.V(0)
    CARDINALITY_OPTIONAL = Field.Cardinality.V(1)
    CARDINALITY_REQUIRED = Field.Cardinality.V(2)
    CARDINALITY_REPEATED = Field.Cardinality.V(3)

    class _Cardinality(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Cardinality.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        CARDINALITY_UNKNOWN = Field.Cardinality.V(0)
        CARDINALITY_OPTIONAL = Field.Cardinality.V(1)
        CARDINALITY_REQUIRED = Field.Cardinality.V(2)
        CARDINALITY_REPEATED = Field.Cardinality.V(3)

    KIND_FIELD_NUMBER: builtins.int
    CARDINALITY_FIELD_NUMBER: builtins.int
    NUMBER_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    TYPE_URL_FIELD_NUMBER: builtins.int
    ONEOF_INDEX_FIELD_NUMBER: builtins.int
    PACKED_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    JSON_NAME_FIELD_NUMBER: builtins.int
    DEFAULT_VALUE_FIELD_NUMBER: builtins.int
    kind: global___Field.Kind.V = ...
    cardinality: global___Field.Cardinality.V = ...
    number: builtins.int = ...
    name: typing.Text = ...
    type_url: typing.Text = ...
    oneof_index: builtins.int = ...
    packed: builtins.bool = ...
    json_name: typing.Text = ...
    default_value: typing.Text = ...

    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Option]: ...

    def __init__(self,
        *,
        kind : global___Field.Kind.V = ...,
        cardinality : global___Field.Cardinality.V = ...,
        number : builtins.int = ...,
        name : typing.Text = ...,
        type_url : typing.Text = ...,
        oneof_index : builtins.int = ...,
        packed : builtins.bool = ...,
        options : typing.Optional[typing.Iterable[global___Option]] = ...,
        json_name : typing.Text = ...,
        default_value : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cardinality",b"cardinality",u"default_value",b"default_value",u"json_name",b"json_name",u"kind",b"kind",u"name",b"name",u"number",b"number",u"oneof_index",b"oneof_index",u"options",b"options",u"packed",b"packed",u"type_url",b"type_url"]) -> None: ...
global___Field = Field

class Enum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    ENUMVALUE_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    SOURCE_CONTEXT_FIELD_NUMBER: builtins.int
    SYNTAX_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    syntax: global___Syntax.V = ...

    @property
    def enumvalue(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___EnumValue]: ...

    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Option]: ...

    @property
    def source_context(self) -> google.protobuf.source_context_pb2.SourceContext: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        enumvalue : typing.Optional[typing.Iterable[global___EnumValue]] = ...,
        options : typing.Optional[typing.Iterable[global___Option]] = ...,
        source_context : typing.Optional[google.protobuf.source_context_pb2.SourceContext] = ...,
        syntax : global___Syntax.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"source_context",b"source_context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"enumvalue",b"enumvalue",u"name",b"name",u"options",b"options",u"source_context",b"source_context",u"syntax",b"syntax"]) -> None: ...
global___Enum = Enum

class EnumValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    NUMBER_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    number: builtins.int = ...

    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Option]: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        number : builtins.int = ...,
        options : typing.Optional[typing.Iterable[global___Option]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"number",b"number",u"options",b"options"]) -> None: ...
global___EnumValue = EnumValue

class Option(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    @property
    def value(self) -> google.protobuf.any_pb2.Any: ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        value : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"value",b"value"]) -> None: ...
global___Option = Option