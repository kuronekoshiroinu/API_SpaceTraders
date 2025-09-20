from dataclasses import dataclass

from domain.entities.ship_available_info_types import ShipAvailableInfoTypes
from domain.entities.ship_info import ShipInfo


@dataclass
class ShipsAvailable:
    modifications_fee: int
    ships_types: list[ShipAvailableInfoTypes]
    ships: list[ShipInfo]
    symbol: str
    transactions: list

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            modifications_fee=data["modificationsFee"],
            ships_types=ShipAvailableInfoTypes.from_list(data["shipTypes"]),
            ships=ShipInfo.from_list(data["ships"]),
            symbol=data["symbol"],
            transactions=data["transactions"],
        )
