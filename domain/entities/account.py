from dataclasses import dataclass

@dataclass
class Account():
    id: str
    credits: int
    headquarters: str
    ship_count: int
    starting_faction: str
    symbol: str