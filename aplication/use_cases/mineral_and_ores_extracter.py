from dataclasses import dataclass
from domain.interfaces import UseCase
import requests
from domain.constants import BASE_URL, AUTHORIZATION_HEADERS


@dataclass
class MineralAndOresExtracter(UseCase):
    mining_ship_symbol: str

    def execute(self, *args, **kwargs):
        response = requests.post(f"{BASE_URL}/my/ships/{self.mining_ship_symbol}/extract",
                                 headers=AUTHORIZATION_HEADERS)
        return response.json()
        # if response.status_code == 200:
        #     #return self._parse_ship_refueler(response.json())
        #      return response.json()
        # else:
        #     raise ValueError(f"Error al obtener datos: {response.status_code}")


if __name__=="__main__":
    from pprint import pprint
    flyer=MineralAndOresExtracter("AGENT_BLUE-6").execute()
    pprint(flyer)