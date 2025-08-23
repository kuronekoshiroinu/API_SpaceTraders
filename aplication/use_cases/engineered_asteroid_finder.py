from dataclasses import dataclass

from domain.entities.engineered_asteroid import EngineeredAsteroid
from domain.entities.engineered_asteroid_chart import EngineeredAsteroidChart
from domain.entities.engineered_asteroid_faction import EngineeredAsteroidFaction
from domain.interfaces import UseCase
from domain.constants import BASE_URL,ACCOUNT_HEADERS
import requests

@dataclass
class EngineeredAsteroidFinder(UseCase):
    system_symbol: str

    def execute(self, *args, **kwargs):
        response = requests.get(f"{BASE_URL}/systems/{self.system_symbol}/waypoints?type=ENGINEERED_ASTEROID")                                #headers=AUTHORIZATION_HEADERS)
        #return response.json()
        if response.status_code == 200:
            return self._parse_engineered_asteroid_data(response.json()["data"])
        else:
            raise ValueError(f"Error al obtener datos: {response.status_code}")

    def _parse_engineered_asteroid_data(self, asteroids_data: list[dict])-> list[EngineeredAsteroid]:
        asteroids=[]
        for asteroid_data in asteroids_data:
            asteroids.append(
                EngineeredAsteroid(
                    chart=self._get_engineered_asteroid_chart(asteroid_data["chart"]),
                    faction=self._get_engineered_asteroid_faction(asteroid_data["faction"]),
                    is_under_construction=asteroid_data["isUnderConstruction"],
                    modifiers=asteroid_data["modifiers"],
                    orbitals=asteroid_data["orbitals"],
                    symbol=asteroid_data["symbol"],
                    system_symbol=asteroid_data["systemSymbol"],
                    traits=asteroid_data["traits"],
                    type=asteroid_data["type"],
                    x=asteroid_data["x"],
                    y=asteroid_data["y"]
                )
            )
        return asteroids

    @classmethod
    def _get_engineered_asteroid_chart(cls, asteroid_chart:dict)->EngineeredAsteroidChart:
        return EngineeredAsteroidChart(
            submitted_by=asteroid_chart["submittedBy"],
            submitted_on=asteroid_chart["submittedOn"],
            waypoint_symbol=asteroid_chart["waypointSymbol"]
        )
    @classmethod
    def _get_engineered_asteroid_faction(cls, asteroid_faction:dict)->EngineeredAsteroidFaction:
        return EngineeredAsteroidFaction(symbol=asteroid_faction["symbol"])





if __name__ == "__main__":
    from pprint import pprint
    asteroide=EngineeredAsteroidFinder("X1-MD96").execute()
    pprint(asteroide)
