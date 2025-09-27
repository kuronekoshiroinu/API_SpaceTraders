from dataclasses import dataclass

@dataclass
class ExtractOreExtractionYield():
    symbol: str
    units: int

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            symbol=data["symbol"],
            units=data["units"],
        )