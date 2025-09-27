from dataclasses import dataclass

from domain.entities.extract_ore_cargo import ExtractOreCargo
from domain.entities.extract_ore_cooldown import ExtractOreCooldown
from domain.entities.extract_ore_extraction import ExtractOreExtraction


@dataclass
class ExtractOre:
    cargo: ExtractOreCargo
    cooldown: ExtractOreCooldown
    events: list
    extraction: ExtractOreExtraction
    modifiers: list

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            cargo=ExtractOreCargo.from_dict(data["cargo"]),
            cooldown=ExtractOreCooldown.from_dict(data["cooldown"]),
            events= data["events"],
            extraction=ExtractOreExtraction.from_dict(data["extraction"]),
            modifiers= data["modifiers"],
        )
