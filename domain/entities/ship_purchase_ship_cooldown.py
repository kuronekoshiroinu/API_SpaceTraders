from dataclasses import dataclass

@dataclass
class ShipPurchaseShipCooldown:
    remaining_seconds: int
    ship_symbol: str
    total_seconds: int