from dataclasses import dataclass
from decimal import Decimal

import jsons

THOUSAND = Decimal(1000)

@dataclass
class Milliunit:
    _value: Decimal

    def __init__(self, value: int):
        self._value = Decimal(value)

    @property
    def value(self) -> Decimal:
        return self._value / THOUSAND


def deserialize_milliunit(obj: int, cls: type = Milliunit, **kwargs) -> Milliunit:
    return Milliunit(obj)


jsons.set_deserializer(deserialize_milliunit, Milliunit)
