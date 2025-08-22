from dataclasses import dataclass

from domain.entities.ship_info_requirements import ShipInfoRequirements


@dataclass
class ShipInfoMounts:
    description: str
    name: str
    requirements: ShipInfoRequirements
    strength: int
    symbol: str
    deposits: list = None
