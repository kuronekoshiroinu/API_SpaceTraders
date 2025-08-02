from pprint import pprint
from dataclasses import dataclass
from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
from domain.entities.shipyard import Shipyard
from domain.entities.shipyard_chart import ShipyardChart
from domain.entities.shipyard_faction import ShipyardFaction
from domain.interfaces import UseCase
import requests
from aplication.use_cases.contract_getter import ContractGetter


@dataclass
class ShipyardFinder(UseCase):
    system_symbol: str

    def execute(self, *args, **kwargs) -> list[Shipyard]:
        response = requests.get(f"{BASE_URL}/systems/{self.system_symbol}/waypoints?traits=SHIPYARD",
                                headers=AUTHORIZATION_HEADERS)
        if response.status_code == 200:
            return self._parse_shipyard_data(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

    def _parse_shipyard_data(self, shipyards_data: list[dict]) -> list[Shipyard]:
        shipyards = []
        for shipyard_data in shipyards_data:
            shipyards.append(
                Shipyard(
                    chart=self._get_shipyard_chart(shipyard_data["chart"]),
                    faction=self._get_shipyard_faction(shipyard_data["faction"]),
                    is_under_construction=shipyard_data["isUnderConstruction"],
                    modifiers=shipyard_data["modifiers"],
                    orbitals=shipyard_data["orbitals"],
                    orbits=shipyard_data["orbits"],
                    symbol=shipyard_data["symbol"],
                    system_symbol=shipyard_data["systemSymbol"],
                    type=shipyard_data["type"],
                )
            )
        return shipyards

    @classmethod
    def _get_shipyard_chart(cls, shipyard_chart: dict) -> ShipyardChart:
        return ShipyardChart(
            submitted_by=shipyard_chart["submittedBy"],
            submitted_on=shipyard_chart["submittedOn"],
            waypoint_symbol=shipyard_chart["waypointSymbol"]
        )

    @classmethod
    def _get_shipyard_faction(cls, shipyard_faction: dict) -> ShipyardFaction:
        return ShipyardFaction(
            symbol=shipyard_faction["symbol"]
        )


if __name__ == "__main__":
    contracts = ContractGetter().execute()
    shipyard_info = ShipyardFinder(contracts[0].terms.deliver[0].system_symbol).execute()
    pprint(shipyard_info)
    # print(type(shipyard_info))
