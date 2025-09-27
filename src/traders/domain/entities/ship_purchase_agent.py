from dataclasses import dataclass

@dataclass
class ShipPurchaseAgent:
    account_id: str
    credits: int
    headquarters: str
    ship_count: int
    starting_faction: str
    symbol: str

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            account_id=data["accountId"],
            credits=data["credits"],
            headquarters=data["headquarters"],
            ship_count=data["shipCount"],
            starting_faction=data["startingFaction"],
            symbol=data["symbol"]
        )