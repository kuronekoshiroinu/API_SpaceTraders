from dataclasses import dataclass

@dataclass
class ShipPurchaseShipUbication:
    symbol: str
    system_symbol: str
    type: str
    x: int
    y: int