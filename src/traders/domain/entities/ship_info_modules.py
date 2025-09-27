from dataclasses import dataclass

from src.traders.domain.entities.ship_info_requirements import ShipInfoRequirements


@dataclass
class ShipInfoModules:
    description: str
    name: str
    requirements: ShipInfoRequirements
    symbol: str
    capacity: int|None = None

    @classmethod
    def from_list(cls, modules_data: list[dict]) -> list["ShipInfoModules"]:
        ships_info_modules = []
        for module in modules_data:
            ships_info_modules.append(
                cls(
                    description=module["description"],
                    name=module["name"],
                    requirements=ShipInfoRequirements.from_dict(module["requirements"]),
                    symbol=module["symbol"],
                    capacity=module.get("capacity"),
                )
            )
        return ships_info_modules
