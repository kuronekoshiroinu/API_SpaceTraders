from dataclasses import dataclass

@dataclass
class ShipyardFaction:
    symbol: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            symbol=data["symbol"]
        )