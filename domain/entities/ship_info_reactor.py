from dataclasses import dataclass
from domain.entities.ship_info_requirements import ShipInfoRequirements


@dataclass
class ShipInfoReactor:
    condition: int
    description: str
    integrity: int
    name : str
    power_output: int
    quality: int
    requirements: ShipInfoRequirements
    symbol: str