from dataclasses import dataclass

@dataclass
class ShipPurchaseShipCargo:
    capacity: int
    inventory: list
    units: int