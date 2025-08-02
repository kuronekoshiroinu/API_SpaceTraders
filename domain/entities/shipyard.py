from dataclasses import dataclass
from domain.entities.shipyard_chart import ShipyardChart
from domain.entities.shipyard_faction import ShipyardFaction

@dataclass
class Shipyard:
    chart: ShipyardChart
    faction: ShipyardFaction
    is_under_construction: bool
    modifiers: list
    orbitals: list
    orbits: str
    symbol: str
    system_symbol: str
    type: str