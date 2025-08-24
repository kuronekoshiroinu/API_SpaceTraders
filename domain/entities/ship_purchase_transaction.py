from dataclasses import dataclass

@dataclass
class ShipPurchaseTransaction:
    agent_symbol: str
    price: int
    ship_symbol: str
    ship_type: str
    timestamp: str
    waypoint_symbol: str