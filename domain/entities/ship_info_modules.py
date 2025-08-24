from dataclasses import dataclass

from domain.entities.ship_info_requirements import ShipInfoRequirements


@dataclass
class ShipInfoModules:
    description: str
    name: str
    requirements: ShipInfoRequirements
    symbol: str
    capacity: int|None = None