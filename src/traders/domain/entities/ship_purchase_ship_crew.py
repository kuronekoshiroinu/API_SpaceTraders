from dataclasses import dataclass
from src.traders.domain.entities.ship_info_crew import ShipInfoCrew

@dataclass
class ShipPurchaseShipCrew(ShipInfoCrew):
    current: int
    morale: int
    rotation: str
    wages: int

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            current=data["current"],
            morale=data["morale"],
            rotation=data["rotation"],
            wages=data["wages"],
            capacity=data["capacity"],
            required=data["required"],
        )