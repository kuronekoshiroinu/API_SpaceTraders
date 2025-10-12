from dataclasses import dataclass

@dataclass
class ShipPurchaseShipCooldown:
    remaining_seconds: int
    ship_symbol: str
    total_seconds: int

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            remaining_seconds=data["remainingSeconds"],
            ship_symbol=data["shipSymbol"],
            total_seconds= data["totalSeconds"],
        )