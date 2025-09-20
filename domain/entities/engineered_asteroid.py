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

    @classmethod
    def from_dict(cls, data:dict):
        return cls(
                    chart=EngineeredAsteroidChart.from_dict(data["chart"]),
                    faction=EngineeredAsteroidFaction.from_dict(data["faction"]),
                    is_under_construction=data["isUnderConstruction"],
                    modifiers=data["modifiers"],
                    orbitals=data["orbitals"],
                    symbol=data["symbol"],
                    system_symbol=data["systemSymbol"],
                    traits=data["traits"],
                    type=data["type"],
                    x=data["x"],
                    y=data["y"]
                )