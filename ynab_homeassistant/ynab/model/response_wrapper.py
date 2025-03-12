from dataclasses import dataclass
from typing import Generic, Type, TypeVar

T = TypeVar("T")

@dataclass
class ResponseWrapper(Generic[T]):
    data: Type[T]
