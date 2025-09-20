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

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            condition=data["condition"],
            description=data["description"],
            integrity=data["integrity"],
            name=data["name"],
            quality=data["quality"],
            requirements=ShipInfoRequirements.from_dict(data["requirements"]),
            speed=data["speed"],
            symbol=data["symbol"]
        )