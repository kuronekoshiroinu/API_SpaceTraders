from dataclasses import dataclass
from domain.entities.ship_available_info_types import ShipAvailableInfoTypes


@dataclass
class ShipAvailableInfo:
    activity: str
    ship_types: list[ShipAvailableInfoTypes]
    ships: list[Ship]
    symbol: str
    transaction: list