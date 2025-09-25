from dataclasses import dataclass
from pprint import pprint

import requests

from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
from domain.entities.shipyard import Shipyard
from domain.interfaces import UseCase


@dataclass
class ShipyardFinder(UseCase):
    system_symbol: str

    def execute(self, *args, **kwargs) -> list[Shipyard]:
        response = requests.get(f"{BASE_URL}/systems/{self.system_symbol}/waypoints?traits=SHIPYARD",
                                headers=AUTHORIZATION_HEADERS)
        if response.status_code == 200:
            return Shipyard.from_list(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")


if __name__ == "__main__":
    from infraestructure.services.space_traders_service import SpaceTradersService

    contracts = SpaceTradersService().get_contract()

    shipyard_info = ShipyardFinder(contracts[0].terms.deliver[0].system_symbol).execute()
    pprint(shipyard_info)
    # print(type(shipyard_info))
