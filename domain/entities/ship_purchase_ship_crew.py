from dataclasses import dataclass
from domain.entities.ship_info_crew import ShipInfoCrew

@dataclass
class ShipPurchaseShipCrew(ShipInfoCrew):
    current: int
    morale: int
    rotation: str
    wages: int