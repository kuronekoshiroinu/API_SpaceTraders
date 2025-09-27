from dataclasses import dataclass

from src.traders.domain.entities.extract_ore_cargo_inventory import ExtractOreCargoInventory


@dataclass
class ExtractOreCargo:
    capacity: int
    inventory: list[ExtractOreCargoInventory]
    units: int

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
            capacity= data["capacity"],
            inventory= ExtractOreCargoInventory.from_list(data["inventory"]),
            units= data["units"],
        )