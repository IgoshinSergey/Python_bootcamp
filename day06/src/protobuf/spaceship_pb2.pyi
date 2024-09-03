from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Ally: _ClassVar[Alignment]
    Enemy: _ClassVar[Alignment]

class ClassShip(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Corvette: _ClassVar[ClassShip]
    Frigate: _ClassVar[ClassShip]
    Cruiser: _ClassVar[ClassShip]
    Destroyer: _ClassVar[ClassShip]
    Carrier: _ClassVar[ClassShip]
    Dreadnought: _ClassVar[ClassShip]
Ally: Alignment
Enemy: Alignment
Corvette: ClassShip
Frigate: ClassShip
Cruiser: ClassShip
Destroyer: ClassShip
Carrier: ClassShip
Dreadnought: ClassShip

class Officer(_message.Message):
    __slots__ = ("first_name", "last_name", "rank")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    rank: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., rank: _Optional[str] = ...) -> None: ...

class Coordinates(_message.Message):
    __slots__ = ("coord",)
    COORD_FIELD_NUMBER: _ClassVar[int]
    coord: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, coord: _Optional[_Iterable[float]] = ...) -> None: ...

class Spaceship(_message.Message):
    __slots__ = ("alignment", "name", "class_ship", "length", "crew_size", "armed", "officers")
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLASS_SHIP_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    CREW_SIZE_FIELD_NUMBER: _ClassVar[int]
    ARMED_FIELD_NUMBER: _ClassVar[int]
    OFFICERS_FIELD_NUMBER: _ClassVar[int]
    alignment: Alignment
    name: str
    class_ship: ClassShip
    length: float
    crew_size: int
    armed: bool
    officers: _containers.RepeatedCompositeFieldContainer[Officer]
    def __init__(self, alignment: _Optional[_Union[Alignment, str]] = ..., name: _Optional[str] = ..., class_ship: _Optional[_Union[ClassShip, str]] = ..., length: _Optional[float] = ..., crew_size: _Optional[int] = ..., armed: bool = ..., officers: _Optional[_Iterable[_Union[Officer, _Mapping]]] = ...) -> None: ...
