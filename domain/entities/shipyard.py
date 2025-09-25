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

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
                    chart=ShipyardChart.from_dict(data["chart"]),
                    faction=ShipyardFaction.from_dict(data["faction"]),
                    is_under_construction=data["isUnderConstruction"],
                    modifiers=data["modifiers"],
                    orbitals=data["orbitals"],
                    orbits=data["orbits"],
                    symbol=data["symbol"],
                    system_symbol=data["systemSymbol"],
                    type=data["type"],
                )

    @classmethod
    def from_list(cls, shipyards_data_list: list[dict]) -> list["Shipyard"]:
        shipyards = []
        for shipyard_data_dict in shipyards_data_list:
            shipyards.append(
                cls.from_dict(shipyard_data_dict)
            )
        return shipyards