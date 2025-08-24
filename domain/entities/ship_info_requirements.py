from dataclasses import dataclass


@dataclass
class ShipInfoRequirements:
    crew: int|None = None
    power: int|None = None
    slots: int|None = None
