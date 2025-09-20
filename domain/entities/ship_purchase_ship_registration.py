from dataclasses import dataclass

@dataclass
class ShipPurchaseShipRegistration:
    faction_symbol: str
    name: str
    role: str

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            faction_symbol=data["factionSymbol"],
            name=data["name"],
            role=data["role"],
        )