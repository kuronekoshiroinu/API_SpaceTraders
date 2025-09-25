from dataclasses import dataclass

import requests

from domain.constants import BASE_URL
from domain.entities.engineered_asteroid import EngineeredAsteroid
from domain.interfaces import UseCase


@dataclass
class EngineeredAsteroidFinder(UseCase):
    system_symbol: str

    def execute(self, *args, **kwargs):
        response = requests.get(f"{BASE_URL}/systems/{self.system_symbol}/waypoints?type=ENGINEERED_ASTEROID")
        if response.status_code == 200:
            return EngineeredAsteroid.from_list(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

if __name__ == "__main__":
    from pprint import pprint

    asteroide = EngineeredAsteroidFinder("X1-CY20").execute()
    pprint(asteroide)
