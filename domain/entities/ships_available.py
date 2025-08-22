from dataclasses import dataclass

from domain.entities.ship_available_info_types import ShipAvailableInfoTypes
from domain.entities.ship_info import ShipInfo


@dataclass
class ShipsAvailable:
    modifications_fee: int
    ships_types: list[ShipAvailableInfoTypes]
    ships: list[ShipInfo]
    symbol: str
    transactions:list