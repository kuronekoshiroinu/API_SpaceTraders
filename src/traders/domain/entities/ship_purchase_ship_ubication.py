from dataclasses import dataclass

@dataclass
class ShipPurchaseShipUbication:
    symbol: str
    system_symbol: str
    type: str
    x: int
    y: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            symbol=data["symbol"],
            system_symbol=data["systemSymbol"],
            type=data["type"],
            x=data["x"],
            y=data["y"]
        )