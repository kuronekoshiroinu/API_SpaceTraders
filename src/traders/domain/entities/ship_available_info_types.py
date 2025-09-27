from dataclasses import dataclass

@dataclass
class ShipAvailableInfoTypes:
    type: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            type=data["type"]
        )

    @classmethod
    def from_list(cls, ships_available: list[dict]) -> list["ShipAvailableInfoTypes"]:
        availables = []
        for ship_available in ships_available:
            availables.append(
                cls.from_dict(ship_available)
            )
        return availables