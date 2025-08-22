from dataclasses import dataclass

@dataclass
class ShipPurchaseAgent:
    account_id: str
    credits: int
    headquarters: str
    ship_count: int
    starting_faction: str
    symbol: str