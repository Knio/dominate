from typing import List, overload, Any, Callable, TypeVar, TypeVarTuple, Type, Tuple, Dict, Literal, Iterable, Self
from numbers import Number


A = TypeVarTuple("A")
R = TypeVar("R")
T = TypeVar("T")
C = TypeVar("C", bound="dom_tag")

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
    def __new__(cls, *args: "dom_tag" | str | Number, **kwargs: str | Literal[True]) -> Self:
        ...

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

    def __call__(self, func: Callable[[*A], R]) -> Callable[[*A], R | Self]:
        ...

    @overload
    def set_attribute(self, key: str, value: str) -> None:
        ...

    @overload
    def set_attribute(self, key: int, value: str | "dom_tag") -> None:
        ...

    def delete_attribute(self, key: str | int) -> None:
        ...

    def add(self, *args: "dom_tag" | str | Number | Dict[str | int, str | "dom_tag" | Literal[True]]) -> None:
        ...

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
    def get(self, tag: Type[T], **kwargs: str | Literal[True]) -> List[T]:
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

def attr(key: str, value: str) -> None:
    ...

@overload
def get_current() -> "dom_tag":
    ...

@overload
def get_current(default: T = ...) -> T | "dom_tag":
    ...
