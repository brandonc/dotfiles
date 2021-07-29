import types
from _weakrefset import WeakSet as WeakSet
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    Mapping,
    MutableMapping,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from _weakref import (
    CallableProxyType as CallableProxyType,
    ProxyType as ProxyType,
    ReferenceType as ReferenceType,
    getweakrefcount as getweakrefcount,
    getweakrefs as getweakrefs,
    proxy as proxy,
    ref as ref,
)

_S = TypeVar("_S")
_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

ProxyTypes: Tuple[Type[Any], ...]

class WeakMethod(ref[types.MethodType]):
    def __new__(cls, meth: types.MethodType, callback: Optional[Callable[[types.MethodType], Any]] = ...) -> WeakMethod: ...
    def __call__(self) -> Optional[types.MethodType]: ...

class WeakValueDictionary(MutableMapping[_KT, _VT]):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __other: Union[Mapping[_KT, _VT], Iterable[Tuple[_KT, _VT]]], **kwargs: _VT) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, k: _KT) -> _VT: ...
    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    def __delitem__(self, v: _KT) -> None: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __str__(self) -> str: ...
    def copy(self) -> WeakValueDictionary[_KT, _VT]: ...
    # These are incompatible with Mapping
    def keys(self) -> Iterator[_KT]: ...  # type: ignore
    def values(self) -> Iterator[_VT]: ...  # type: ignore
    def items(self) -> Iterator[Tuple[_KT, _VT]]: ...  # type: ignore
    def itervaluerefs(self) -> Iterator[KeyedRef[_KT, _VT]]: ...
    def valuerefs(self) -> List[KeyedRef[_KT, _VT]]: ...

class KeyedRef(ref[_T], Generic[_KT, _T]):
    key: _KT
    # This __new__ method uses a non-standard name for the "cls" parameter
    def __new__(type, ob: _T, callback: Callable[[_T], Any], key: _KT) -> KeyedRef[_KT, _T]: ...  # type: ignore
    def __init__(self, ob: _T, callback: Callable[[_T], Any], key: _KT) -> None: ...

class WeakKeyDictionary(MutableMapping[_KT, _VT]):
    @overload
    def __init__(self, dict: None = ...) -> None: ...
    @overload
    def __init__(self, dict: Union[Mapping[_KT, _VT], Iterable[Tuple[_KT, _VT]]]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, k: _KT) -> _VT: ...
    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    def __delitem__(self, v: _KT) -> None: ...
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __str__(self) -> str: ...
    def copy(self) -> WeakKeyDictionary[_KT, _VT]: ...
    # These are incompatible with Mapping
    def keys(self) -> Iterator[_KT]: ...  # type: ignore
    def values(self) -> Iterator[_VT]: ...  # type: ignore
    def items(self) -> Iterator[Tuple[_KT, _VT]]: ...  # type: ignore
    def keyrefs(self) -> List[ref[_KT]]: ...

class finalize:
    def __init__(self, __obj: object, __func: Callable[..., Any], *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, _: Any = ...) -> Optional[Any]: ...
    def detach(self) -> Optional[Tuple[Any, Any, Tuple[Any, ...], Dict[str, Any]]]: ...
    def peek(self) -> Optional[Tuple[Any, Any, Tuple[Any, ...], Dict[str, Any]]]: ...
    alive: bool
    atexit: bool
