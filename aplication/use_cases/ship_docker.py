from dataclasses import dataclass

import requests

from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
from domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from domain.interfaces import UseCase


@dataclass
class ShipDocker(UseCase):
    mining_ship_symbol: str

    def execute(self, *args, **kwargs):
        response = requests.post(f"{BASE_URL}/my/ships/{self.mining_ship_symbol}/dock",
                                 headers=AUTHORIZATION_HEADERS)
        if response.status_code == 200:
            return self._parse_ship_docker(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")
    def _parse_ship_docker(self, ship_data:dict)->ShipPurchaseShipNav:
        return ShipPurchaseShipNav.from_dict(ship_data["nav"])

if __name__=="__main__":
    from pprint import pprint
    flyer=ShipDocker("AGENT_BLUE-3").execute()
    pprint(flyer)