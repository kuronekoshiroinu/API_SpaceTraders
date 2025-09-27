from dataclasses import dataclass

from src.traders.domain.entities.ship_info_requirements import ShipInfoRequirements


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

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            condition=data["condition"],
            description=data["description"],
            fuel_capacity=data["fuelCapacity"],
            integrity=data["integrity"],
            module_slots=data["moduleSlots"],
            mounting_points=data["mountingPoints"],
            name=data["name"],
            quality=data["quality"],
            requirements=ShipInfoRequirements.from_dict(data["requirements"]),
            symbol=data["symbol"]
        )