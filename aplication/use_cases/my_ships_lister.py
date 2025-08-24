from dataclasses import dataclass
from domain.constants import BASE_URL, AUTHORIZATION_HEADERS
import requests

@dataclass
class MyShipsLister:

    def execute(self, *args, **kwargs) :
        response = requests.get(f"{BASE_URL}/my/ships",
                              headers=AUTHORIZATION_HEADERS)
        return response.json()
        # if response.status_code == 200:
        #     return self._parse_shipyard_data(response.json()["data"])
        # else:
        #     raise ValueError(f"Error al obtener datos: {response.status_code}")


if __name__=="__main__":
    from pprint import pprint
    flyer=MyShipsLister().execute()
    pprint(flyer)
