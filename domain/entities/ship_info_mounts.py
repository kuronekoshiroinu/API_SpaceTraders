from dataclasses import dataclass

from domain.entities.ship_info_requirements import ShipInfoRequirements


@dataclass
class ShipInfoMounts:
    description: str
    name: str
    requirements: ShipInfoRequirements
    strength: int
    symbol: str
    deposits: list = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            description=data["description"],
            name=data["name"],
            requirements=ShipInfoRequirements.from_dict(data["requirements"]),
            strength=data["strength"],
            symbol=data["symbol"],
            deposits=list(data["deposits"]) if data.get("deposits", None) else None,
        )

    @classmethod
    def from_list(cls, mounts_data: list[dict]) -> list["ShipInfoMounts"]:
        mounts = []
        for mount in mounts_data:
            mounts.append(
                cls.from_dict(mount)
            )
        return mounts
