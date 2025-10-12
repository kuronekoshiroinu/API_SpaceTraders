from dataclasses import dataclass

@dataclass
class ToAsteroidNavigateFuelConsumed:
    amount: int
    timestamp: str

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            amount=data["amount"],
            timestamp=data["timestamp"]
        )