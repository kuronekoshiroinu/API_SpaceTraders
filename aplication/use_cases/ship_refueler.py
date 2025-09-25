from dataclasses import dataclass
import requests

from domain.entities.ship_refuel import ShipRefuel
from domain.interfaces import UseCase
from domain.constants import BASE_URL, AUTHORIZATION_HEADERS

@dataclass
class ShipRefueler(UseCase):
    mining_ship_symbol: str

    def execute(self, *args, **kwargs):
        response = requests.post(f"{BASE_URL}/my/ships/{self.mining_ship_symbol}/refuel",
                                 headers=AUTHORIZATION_HEADERS)
        if response.status_code == 200:
            return ShipRefuel.from_dict(response.json()["data"])
            #return response.json()
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

if __name__=="__main__":
    from pprint import pprint
    flyer=ShipRefueler("AGENT_ROUGE-2").execute()
    pprint(flyer)