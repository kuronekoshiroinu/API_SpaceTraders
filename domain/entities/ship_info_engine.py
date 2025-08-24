from dataclasses import dataclass

from domain.entities.ship_info_requirements import ShipInfoRequirements


@dataclass
class ShipInfoEngine:
    condition: int
    description: str
    integrity: int
    name: str
    quality: int
    requirements: ShipInfoRequirements
    speed: int
    symbol: str