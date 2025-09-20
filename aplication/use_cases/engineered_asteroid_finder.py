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
            return self._parse_engineered_asteroid_data(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

    def _parse_engineered_asteroid_data(self, asteroids_data: list[dict]) -> list[EngineeredAsteroid]:
        asteroids = []
        for asteroid_data in asteroids_data:
            asteroids.append(
                EngineeredAsteroid.from_dict(asteroid_data)
            )
        return asteroids


if __name__ == "__main__":
    from pprint import pprint

    asteroide = EngineeredAsteroidFinder("X1-RH66").execute()
    pprint(asteroide)
