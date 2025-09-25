from dataclasses import dataclass

import requests

from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
from domain.entities.ship_purchase_ship_nav import ShipPurchaseShipNav
from domain.entities.ship_purchase_ship_nav_route import ShipPurchaseShipNavRoute


@dataclass
class ShipOrbiter:
    mining_ship_symbol: str

    def execute(self, *args, **kwargs) :
        response = requests.post(f"{BASE_URL}/my/ships/{self.mining_ship_symbol}/orbit",
                              headers=AUTHORIZATION_HEADERS)
        if response.status_code == 200:
            return ShipPurchaseShipNav.from_dict(response.json()["data"]["nav"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

if __name__=="__main__":
    from pprint import pprint
    flyer=ShipOrbiter("AGENT_BLUE-4").execute()
    pprint(flyer)
