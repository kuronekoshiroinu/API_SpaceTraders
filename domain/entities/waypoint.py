from dataclasses import dataclass

@dataclass
class Waypoint:
    chart: dict
    faction: dict
    is_under_construction: bool
    modifiers: list
    orbitals: list
    orbits: str
    symbol: str
    system_symbol: str
    traits: list
    type: str
    x: int
    y: int