from dataclasses import dataclass

@dataclass
class ExtractOreCooldown():
    expiration: str
    remaining_seconds: int
    ship_symbol: str
    total_seconds: int

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            expiration= data["expiration"],
            remaining_seconds= data["remainingSeconds"],
            ship_symbol= data["shipSymbol"],
            total_seconds= data["totalSeconds"],
        )