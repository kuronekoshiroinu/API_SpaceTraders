from dataclasses import dataclass

@dataclass
class ShipPurchaseTransaction:
    agent_symbol: str
    price: int
    ship_symbol: str
    ship_type: str
    timestamp: str
    waypoint_symbol: str

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            agent_symbol= data["agentSymbol"],
            price=data["price"],
            ship_symbol=data["shipSymbol"],
            ship_type=data["shipType"],
            timestamp=data["timestamp"],
            waypoint_symbol=data["waypointSymbol"],
        )

