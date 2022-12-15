from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["author", "genre", "id", "name", "year"]
    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Book.Genre
    id: ISBN
    name: str
    nonfiction: Book.Genre
    selfhelp: Book.Genre
    suspense: Book.Genre
    thriller: Book.Genre
    year: int
    def __init__(self, id: _Optional[_Union[ISBN, _Mapping]] = ..., name: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Book.Genre, str]] = ..., year: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ISBN(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["bk"]
    BK_FIELD_NUMBER: _ClassVar[int]
    bk: Book
    def __init__(self, bk: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...
