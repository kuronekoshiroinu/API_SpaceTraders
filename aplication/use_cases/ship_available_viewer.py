from dataclasses import dataclass
from aplication.use_cases.contract_getter import ContractGetter
from aplication.use_cases.shipyard_finder import ShipyardFinder
from domain.interfaces import UseCase
from domain.constants import BASE_URL, ACCOUNT_HEADERS
import requests

@dataclass
class ShipAvailableViewer(UseCase):
    system_symbol: str
    waypoint_symbol: str

    def execute(self,*args, **kwargs):
        url = f"{BASE_URL}/systems/{self.system_symbol}/waypoints/{self.waypoint_symbol}/shipyard"
        response = requests.get(url, headers=ACCOUNT_HEADERS)
        return response.json()
        # if response.status_code == 200:
        #     return self._parse_ships_availables_data(response.json())
        # else:
        #     error_msg = response.json().get('error', {}).get('message', 'Error desconocido')
        #     raise ValueError(f"Error al obtener shipyard: {error_msg}")

    def _parse_ships_availables_data(self, ships_data:dict):



if __name__ == '__main__':
    from pprint import pprint
    contracts = ContractGetter().execute()
    shipyard_info = ShipyardFinder(contracts[0].terms.deliver[0].system_symbol).execute()
    pprint(shipyard_info)
    #print(shipyard_info)

    ship_availables=ShipAvailableViewer(contracts[0].terms.deliver[0].system_symbol, 'X1-BF56-H48').execute()
    pprint(ship_availables)