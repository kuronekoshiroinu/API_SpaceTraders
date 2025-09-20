from dataclasses import dataclass

import requests

from aplication.use_cases.shipyard_finder import ShipyardFinder
from domain.constants import BASE_URL, ACCOUNT_HEADERS
from domain.entities.ships_available import ShipsAvailable
from domain.interfaces import UseCase


@dataclass
class ShipAvailableViewer(UseCase):
    system_symbol: str
    waypoint_symbol: str

    def execute(self, *args, **kwargs):
        url = f"{BASE_URL}/systems/{self.system_symbol}/waypoints/{self.waypoint_symbol}/shipyard"
        response = requests.get(url, headers=ACCOUNT_HEADERS)
        if response.status_code == 200:
            return self._parse_ships_availables_data(response.json())
        else:
            error_msg = response.json().get('error', {}).get('message', 'Error desconocido')
            raise ValueError(f"Error al obtener ships availables: {error_msg}")

    def _parse_ships_availables_data(self, ships_data: dict) -> ShipsAvailable:
        return ShipsAvailable.from_dict(ships_data["data"])


if __name__ == '__main__':
    from pprint import pprint
    from infraestructure.services.space_traders_service import SpaceTradersService

    contracts = SpaceTradersService().get_contract()

    shipyard_info = ShipyardFinder(contracts[0].terms.deliver[0].system_symbol).execute()
    pprint(shipyard_info)
    # print(shipyard_info[1].symbol)
    ship_availables = ShipAvailableViewer(contracts[0].terms.deliver[0].system_symbol,
                                          shipyard_info[2].symbol).execute()
    pprint(ship_availables)
