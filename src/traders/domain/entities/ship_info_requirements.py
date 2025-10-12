from dataclasses import dataclass


@dataclass
class ShipInfoRequirements:
    crew: int|None = None
    power: int|None = None
    slots: int|None = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            crew=data.get("crew", None),
            power=data.get("power", None),
            slots=data.get("slots", None)
        )
