from dataclasses import dataclass

import requests

from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
from domain.entities.ship_purchase_ship import ShipPurchaseShip


@dataclass
class MyShipsLister:

    def execute(self, *args, **kwargs) :
        response = requests.get(f"{BASE_URL}/my/ships",
                              headers=AUTHORIZATION_HEADERS)
        if response.status_code == 200:
            return self._parse_ship_lister(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")
    @classmethod
    def _parse_ship_lister(cls,data:list[dict])->list[ShipPurchaseShip]:
        ships=[]
        for ship_dict in data:
            ships.append(ShipPurchaseShip.from_dict(ship_dict))
        return ships


if __name__=="__main__":
    from pprint import pprint
    flyer=MyShipsLister().execute()
    pprint(flyer)
