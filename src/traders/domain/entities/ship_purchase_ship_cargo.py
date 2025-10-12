from dataclasses import dataclass

@dataclass
class ShipPurchaseShipCargo:
    capacity: int
    inventory: list
    units: int

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            capacity=data["capacity"],
            inventory=data["inventory"],
            units=data["units"],
        )