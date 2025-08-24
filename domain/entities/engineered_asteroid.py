from dataclasses import dataclass
from domain.entities.engineered_asteroid_chart import EngineeredAsteroidChart
from domain.entities.engineered_asteroid_faction import EngineeredAsteroidFaction


@dataclass
class EngineeredAsteroid:
    chart: EngineeredAsteroidChart
    faction: EngineeredAsteroidFaction
    is_under_construction: bool
    modifiers: list
    orbitals: list
    symbol: str
    system_symbol: str
    traits: list[dict]
    type: str
    x: int
    y: int