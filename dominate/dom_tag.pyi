from typing import List, Unpack, overload, Any, Callable, TypeVar, TypeVarTuple, Type, Tuple, Dict, Literal, Iterable, Self, TypeAlias
from numbers import Number


A = TypeVarTuple("A")
R = TypeVar("R")
T = TypeVar("T")
C = TypeVar("C", bound="dom_tag")

AddArg: TypeAlias = "dom_tag" | str | Number | Dict[str | int, str | "dom_tag" | Literal[True]]

T1 = TypeVar("T1", bound=AddArg)
T2 = TypeVar("T2", bound=AddArg)
T3 = TypeVar("T3", bound=AddArg)
T4 = TypeVar("T4", bound=AddArg)
T5 = TypeVar("T5", bound=AddArg)
T6 = TypeVar("T6", bound=AddArg)

class dom_tag(object):
    is_single: bool
    is_pretty: bool
    is_inline: bool
    children: List["dom_tag" | str]
    parent: "dom_tag" | None

    ### omitting these until https://github.com/python/mypy/issues/15182 is addressed
    # @overload
    # def __new__(_cls, func: "Callable[[*A], None]") -> Callable[[*A], Self]:
    #     ...

    # @overload
    # def __new__(_cls, func: "Callable[[*A], R]") -> Callable[[*A], R | Self]:
    #     ...

    # @overload
    def __new__(
        cls,
        *args: "dom_tag" | str | Number,
        __inline: bool = ...,
        __pretty: bool = ...,
        **kwargs: str | Literal[True]
    ) -> Self: ...

    def __init__(
        self,
        *args: "dom_tag" | str | Number,
        __inline: bool = ...,
        __pretty: bool = ...,
        **kwargs: str | Literal[True],
    ) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        ...

    @overload
    def __call__(self, func: Callable[[*A], None]) -> Callable[[*A], Self]: ...
    @overload
    def __call__(self, func: Callable[[*A], R]) -> Callable[[*A], R | Self]: ...

    @overload
    def set_attribute(self, key: str, value: str) -> None:
        ...

    @overload
    def set_attribute(self, key: int, value: str | "dom_tag") -> None:
        ...

    def delete_attribute(self, key: str | int) -> None:
        ...

    @overload
    def add(self, arg1: T1) -> T1: ...
    @overload
    def add(self, arg1: T1, arg2: T2) -> Tuple[T1, T2]: ...
    @overload
    def add(self, arg1: T1, arg2: T2, arg3: T3) -> Tuple[T1, T2, T3]: ...
    @overload
    def add(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4) -> Tuple[T1, T2, T3, T4]: ...
    @overload
    def add(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5) -> Tuple[T1, T2, T3, T4, T5]: ...
    @overload
    def add(self, arg1: T1, arg2: T2, arg3: T3, arg4: T4, arg5: T5, arg6: T6) -> Tuple[T1, T2, T3, T4, T5, T6]: ...

    def add_raw_string(self, s: str) -> None:
        ...

    def remove(self, obj: "dom_tag" | str) -> None:
        ...

    def clear(self) -> None:
        ...

    @overload
    def get(self, tag: str, **kwargs: str | Literal[True]) -> List["dom_tag" | Any]:
        ...

    @overload
    def get(self, tag: Type[C], **kwargs: str | Literal[True]) -> List[C]:
        ...

    @overload
    def __getitem__(self, key: int) -> "dom_tag" | str:
        ...

    @overload
    def __getitem__(self, key: str) -> str:
        ...

    def __iter__(self) -> Iterable["dom_tag" | str]:
        ...

    def __contains__(self, item: Any) -> bool:
        ...

    def __iadd__(self, other: "dom_tag" | str | Number | Dict[str | int, str | "dom_tag" | Literal[True]]) -> Self:
        ...

    def render(self, indent: int = ..., pretty: bool = ..., xhtml: bool = ...) -> str:
        ...

    @classmethod
    def clean_pair(cls, key: str, value: str | Literal[True]) -> Tuple[str, str]:
        ...


def attr(*args: Dict[str, str | Literal[True]], **kwargs: str | Literal[True]) -> None:
    ...

@overload
def get_current() -> "dom_tag":
    ...

@overload
def get_current(default: T = ...) -> T | "dom_tag":
    ...
