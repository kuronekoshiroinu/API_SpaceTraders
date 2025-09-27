from dataclasses import dataclass
from src.traders.domain.entities.ship_info_requirements import ShipInfoRequirements


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

    @classmethod
    def from_dict(cls, data: dict) :
        return cls(
            condition=data["condition"],
            description=data["description"],
            integrity=data["integrity"],
            name=data["name"],
            power_output=data["powerOutput"],
            quality=data["quality"],
            requirements=ShipInfoRequirements.from_dict(data["requirements"]),
            symbol=data["symbol"],
        )