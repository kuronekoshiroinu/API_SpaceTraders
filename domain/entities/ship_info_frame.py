from dataclasses import dataclass

from domain.entities.ship_info_requirements import ShipInfoRequirements


@dataclass
class ShipInfoFrame:
    condition: int
    description: str
    fuel_capacity: int
    integrity: int
    module_slots: int
    mounting_points: int
    name: str
    quality: int
    requirements: ShipInfoRequirements
    symbol: str