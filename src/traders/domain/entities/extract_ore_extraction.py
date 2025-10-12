from dataclasses import dataclass

from src.traders.domain.entities.extract_ore_extraction_yield import ExtractOreExtractionYield


@dataclass
class ExtractOreExtraction():
    ship_symbol: str
    yield_: ExtractOreExtractionYield

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            ship_symbol=data["shipSymbol"],
            yield_=ExtractOreExtractionYield.from_dict(data["yield"]),
        )