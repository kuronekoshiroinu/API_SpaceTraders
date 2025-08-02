from dataclasses import dataclass

from domain.entities.ships_available_types import ShipsAvailableTypes


@dataclass
class ShipsAvailable:
    modifications_fee: int
    ships_types: list[ShipsAvailableTypes]
    ships: list[ShipAvailableInfo]